from fastapi import APIRouter

from app.db import get_client

router = APIRouter()


@router.get("/health")
def health() -> dict:
    client = get_client()
    shots = client.command("SELECT count() FROM shots")
    films = client.command("SELECT uniqExact(film_id) FROM shots")
    return {"status": "ok", "films": films, "shots": shots}
