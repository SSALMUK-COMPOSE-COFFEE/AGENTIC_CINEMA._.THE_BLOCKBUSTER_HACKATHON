import uuid

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from app.agent.tools.edl import build_edl
from app.db import get_client

router = APIRouter()


class SequenceRequest(BaseModel):
    shot_ids: list[str]
    title: str = "SHOT MEMORY SEQUENCE"
    fps: float = 24.0
    session_id: str = "manual"
    intent: str = "manual timeline"


@router.post("/sequences/edl", response_class=PlainTextResponse)
def edl(req: SequenceRequest) -> str:
    return build_edl(req.shot_ids, req.title, req.fps)["edl"]


@router.post("/sequences/timeline")
def timeline(req: SequenceRequest) -> dict:
    return build_edl(req.shot_ids, req.title, req.fps)


@router.post("/sequences")
def save(req: SequenceRequest) -> dict:
    sequence_id = uuid.uuid4().hex
    get_client().insert(
        "sequences", [[sequence_id, req.session_id, req.intent, req.shot_ids]],
        column_names=["sequence_id", "session_id", "intent", "shot_ids"],
    )
    return {"sequence_id": sequence_id, "shot_count": len(req.shot_ids)}


@router.get("/sequences")
def recent(limit: int = 20) -> list[dict]:
    q = "SELECT sequence_id, session_id, intent, shot_ids, approved, created_at FROM sequences ORDER BY created_at DESC LIMIT %(l)s"
    return list(get_client().query(q, parameters={"l": limit}).named_results())
