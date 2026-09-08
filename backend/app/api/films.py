from pathlib import Path

from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

from app import search
from app.ingest.pipeline import ingest_film

router = APIRouter()


class IngestRequest(BaseModel):
    source: str
    title: str
    year: int
    film_id: str | None = None
    limit: int | None = None


@router.get("/films")
def films() -> list[dict]:
    return search.list_films()


@router.get("/films/{film_id}/shots")
def film_shots(film_id: str, offset: int = 0, limit: int = 60) -> list[dict]:
    return search.list_shots(film_id, offset, limit)


@router.post("/films/ingest", status_code=202)
async def ingest(req: IngestRequest, tasks: BackgroundTasks) -> dict:
    source = Path(req.source)
    if not source.exists():
        raise HTTPException(404, f"source not found: {source}")
    tasks.add_task(ingest_film, source, req.title, req.year, req.film_id, req.limit)
    return {"accepted": True, "title": req.title}


@router.get("/stats")
def stats() -> dict:
    return search.stats()
