import json
from collections.abc import AsyncIterator

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent.agent import root_agent

APP_NAME = "shot-memory"
_session_service = InMemorySessionService()
_runner = Runner(app_name=APP_NAME, agent=root_agent, session_service=_session_service)


async def ensure_session(user_id: str, session_id: str) -> None:
    existing = await _session_service.get_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)
    if existing is None:
        await _session_service.create_session(
            app_name=APP_NAME, user_id=user_id, session_id=session_id, state={"session_id": session_id}
        )


async def stream_chat(user_id: str, session_id: str, message: str) -> AsyncIterator[dict]:
    await ensure_session(user_id, session_id)
    content = types.Content(role="user", parts=[types.Part(text=message)])
    async for event in _runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        for call in event.get_function_calls() or []:
            yield {"type": "tool_call", "agent": event.author, "name": call.name, "args": call.args}
        for resp in event.get_function_responses() or []:
            yield {"type": "tool_result", "agent": event.author, "name": resp.name,
                   "result": _truncate(resp.response)}
        if event.content and event.content.parts:
            text = "".join(p.text for p in event.content.parts if p.text)
            if text:
                yield {"type": "text", "agent": event.author, "text": text, "final": event.is_final_response()}


def _truncate(obj, limit: int = 4000):
    s = json.dumps(obj, default=str)
    return json.loads(s) if len(s) <= limit else {"truncated": s[:limit]}
