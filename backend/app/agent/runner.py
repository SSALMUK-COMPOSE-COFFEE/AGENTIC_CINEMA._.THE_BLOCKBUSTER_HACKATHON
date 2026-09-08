import asyncio
from collections.abc import AsyncIterator

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import trace
from app.agent.agent import root_agent

APP_NAME = "shot-memory"
_session_service = InMemorySessionService()
_runner = Runner(app_name=APP_NAME, agent=root_agent, session_service=_session_service)
_DONE = object()


async def ensure_session(user_id: str, session_id: str) -> None:
    existing = await _session_service.get_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)
    if existing is None:
        await _session_service.create_session(
            app_name=APP_NAME, user_id=user_id, session_id=session_id, state={"session_id": session_id}
        )


async def stream_chat(user_id: str, session_id: str, message: str) -> AsyncIterator[dict]:
    await ensure_session(user_id, session_id)
    queue = trace.start()
    content = types.Content(role="user", parts=[types.Part(text=message)])

    async def run() -> None:
        try:
            async for event in _runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
                if event.content and event.content.parts:
                    text = "".join(p.text for p in event.content.parts if p.text)
                    if text:
                        trace.emit({"type": "text", "agent": event.author, "text": text,
                                    "final": event.is_final_response()})
        except Exception as e:  # noqa: BLE001
            trace.emit({"type": "error", "message": str(e)})
        finally:
            queue.put_nowait(_DONE)

    task = asyncio.create_task(run())
    try:
        while True:
            item = await queue.get()
            if item is _DONE:
                break
            yield item
    finally:
        if not task.done():
            task.cancel()
