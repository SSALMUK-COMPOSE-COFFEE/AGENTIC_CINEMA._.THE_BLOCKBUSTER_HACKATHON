import argparse
import asyncio
import re
import sys
from pathlib import Path

from app.config import settings
from app.db import get_client
from app.ingest.describe import describe_shot
from app.ingest.embed import embed_image
from app.ingest.load import insert_shots, shot_row, upsert_film
from app.ingest.media import make_proxy, make_thumbnails, probe
from app.ingest.scenes import ShotSpan, detect_shots

BATCH = 50


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


async def process_shot(sem: asyncio.Semaphore, src: Path, film_id: str, title: str, span: ShotSpan) -> list | None:
    async with sem:
        shot_name = f"{film_id}_{span.index:05d}"
        proxy = settings.data_dir / "proxies" / film_id / f"{shot_name}.mp4"
        thumb_stem = settings.data_dir / "thumbs" / film_id / shot_name
        try:
            if not proxy.exists():
                await asyncio.to_thread(make_proxy, src, span.t_in, span.t_out, proxy)
            thumbs = await asyncio.to_thread(make_thumbnails, src, span.t_in, span.t_out, thumb_stem)
            meta, embedding = await asyncio.gather(describe_shot(proxy), embed_image(thumbs[1]))
        except Exception as e:  # noqa: BLE001
            print(f"[{film_id}] shot {span.index} failed: {type(e).__name__}: {str(e)[:120]}", file=sys.stderr, flush=True)
            return None
        rel = settings.data_dir
        return shot_row(
            film_id, title, span, meta,
            f"/media/{thumbs[1].relative_to(rel).as_posix()}",
            f"/media/{proxy.relative_to(rel).as_posix()}",
            embedding,
        )


def existing_indexes(client, film_id: str) -> set[int]:
    rows = client.query("SELECT shot_index FROM shots WHERE film_id = %(f)s", parameters={"f": film_id}).result_rows
    return {r[0] for r in rows}


async def ingest_film(source: Path, title: str, year: int, film_id: str | None = None,
                      limit: int | None = None, threshold: float = 15.0) -> str:
    film_id = film_id or slugify(title)
    client = get_client()
    info = probe(source)
    upsert_film(client, film_id, title, year, str(source), info.fps, info.duration, 0, "detecting")

    spans = await asyncio.to_thread(detect_shots, str(source), threshold)
    if limit:
        spans = spans[:limit]
    total = len(spans)
    done_idx = existing_indexes(client, film_id)
    spans = [s for s in spans if s.index not in done_idx]
    upsert_film(client, film_id, title, year, str(source), info.fps, info.duration, total, "describing")
    print(f"[{film_id}] {total} shots detected, {len(done_idx)} already loaded, {len(spans)} to go", flush=True)

    sem = asyncio.Semaphore(settings.ingest_concurrency)
    done = len(done_idx)
    failed = 0
    for start in range(0, len(spans), BATCH):
        chunk = spans[start:start + BATCH]
        rows = await asyncio.gather(*(process_shot(sem, source, film_id, title, s) for s in chunk))
        ok = [r for r in rows if r is not None]
        failed += len(rows) - len(ok)
        insert_shots(client, ok)
        done += len(ok)
        print(f"[{film_id}] {done}/{total} shots loaded ({failed} failed)", flush=True)

    upsert_film(client, film_id, title, year, str(source), info.fps, info.duration, total, "done")
    return film_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a film into Shot Memory")
    parser.add_argument("source", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--film-id")
    parser.add_argument("--limit", type=int, help="only process the first N shots")
    parser.add_argument("--threshold", type=float, default=15.0, help="PySceneDetect content threshold")
    args = parser.parse_args()
    film_id = asyncio.run(ingest_film(args.source, args.title, args.year, args.film_id, args.limit, args.threshold))
    print(f"done: {film_id}")


if __name__ == "__main__":
    main()
