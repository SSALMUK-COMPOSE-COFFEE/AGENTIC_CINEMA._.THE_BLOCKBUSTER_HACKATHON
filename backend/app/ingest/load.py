from datetime import UTC, datetime

from clickhouse_connect.driver.client import Client

from app.ingest.scenes import ShotSpan
from app.ingest.schema import ShotMeta

SHOT_COLUMNS = [
    "film_id", "film_title", "shot_id", "shot_index", "t_in", "t_out", "caption", "people_count",
    "time_of_day", "interior", "weather", "shot_size", "camera_move", "emotion", "tension",
    "dialogue_present", "dominant_colors", "objects", "characters", "thumbnail_uri", "proxy_uri", "embedding",
]


def shot_row(film_id: str, film_title: str, span: ShotSpan, meta: ShotMeta,
             thumbnail_uri: str, proxy_uri: str, embedding: list[float]) -> list:
    return [
        film_id, film_title, f"{film_id}:{span.index:05d}", span.index, span.t_in, span.t_out,
        meta.caption, meta.people_count, meta.time_of_day.value, meta.interior.value, meta.weather,
        meta.shot_size.value, meta.camera_move.value, meta.emotion, meta.tension, meta.dialogue_present,
        meta.dominant_colors, meta.objects, meta.characters, thumbnail_uri, proxy_uri, embedding,
    ]


def insert_shots(client: Client, rows: list[list]) -> None:
    if rows:
        client.insert("shots", rows, column_names=SHOT_COLUMNS)


def upsert_film(client: Client, film_id: str, title: str, year: int, source_uri: str,
                fps: float, duration: float, shot_count: int, status: str) -> None:
    now = datetime.now(UTC)
    client.insert(
        "films",
        [[film_id, title, year, source_uri, fps, duration, shot_count, status, now, now]],
        column_names=["film_id", "title", "year", "source_uri", "fps", "duration", "shot_count", "status",
                      "created_at", "updated_at"],
    )
