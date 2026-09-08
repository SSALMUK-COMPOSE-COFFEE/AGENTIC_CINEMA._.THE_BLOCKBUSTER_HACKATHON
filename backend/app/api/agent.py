import json
import uuid

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.agent.runner import stream_chat

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None
    user_id: str = "editor"


@router.post("/agent/chat")
async def chat(req: ChatRequest) -> StreamingResponse:
    session_id = req.session_id or uuid.uuid4().hex

    async def gen():
        yield f"data: {json.dumps({'type': 'session', 'session_id': session_id})}\n\n"
        try:
            async for ev in stream_chat(req.user_id, session_id, req.message):
                yield f"data: {json.dumps(ev, default=str)}\n\n"
        except Exception as e:  # noqa: BLE001
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"
        yield "data: {\"type\": \"done\"}\n\n"

    return StreamingResponse(gen(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
