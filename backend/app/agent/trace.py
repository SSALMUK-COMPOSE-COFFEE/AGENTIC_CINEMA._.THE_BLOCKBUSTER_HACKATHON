import asyncio
import json
import re
import time
from contextvars import ContextVar
from typing import Any

from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

from app import search
from app.agent.tools.edl import build_edl

_queue: ContextVar[asyncio.Queue | None] = ContextVar("trace_queue", default=None)
_t0: ContextVar[float] = ContextVar("trace_t0", default=0.0)
_started: dict[str, float] = {}
_FENCE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$")


def start() -> asyncio.Queue:
    q: asyncio.Queue = asyncio.Queue()
    _queue.set(q)
    _t0.set(time.monotonic())
    return q


def emit(event: dict[str, Any]) -> None:
    q = _queue.get()
    if q is not None:
        event["t"] = round(time.monotonic() - _t0.get(), 2)
        q.put_nowait(event)


def truncate(obj: Any, limit: int = 4000) -> Any:
    s = json.dumps(obj, default=str)
    return json.loads(s) if len(s) <= limit else {"truncated": s[:limit]}


def parse_json(text: Any) -> dict | None:
    if isinstance(text, dict):
        return text
    if not isinstance(text, str):
        return None
    cleaned = _FENCE.sub("", text)
    start = cleaned.find("{")
    if start < 0:
        return None
    depth = 0
    for i in range(start, len(cleaned)):
        if cleaned[i] == "{":
            depth += 1
        elif cleaned[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(cleaned[start:i + 1])
                except json.JSONDecodeError:
                    return None
    return None


def hydrate_librarian(data: dict) -> dict:
    ids = [s for s in data.get("shot_ids", []) if isinstance(s, str)]
    shots = search.get_shots(ids) if ids else []
    return {"sql": data.get("sql", ""), "count": len(shots), "shots": shots}


def hydrate_assembler(data: dict) -> dict:
    ids = [s for s in data.get("shot_ids", []) if isinstance(s, str)]
    built = build_edl(ids, "SHOT MEMORY SEQUENCE") if ids else {"edl": "", "timeline": [], "total_seconds": 0}
    return {
        "brief": data.get("brief", ""),
        "beats": data.get("beats", []),
        "shot_ids": ids,
        "warnings": data.get("warnings", []),
        "sequence_id": data.get("sequence_id"),
        **built,
    }


HYDRATORS = {"Librarian": hydrate_librarian, "CutAssembler": hydrate_assembler}


def before_tool(tool: BaseTool, args: dict, tool_context: ToolContext) -> None:
    if tool_context.function_call_id:
        _started[tool_context.function_call_id] = time.monotonic()
    emit({"type": "tool_call", "agent": tool_context.agent_name, "name": tool.name, "args": truncate(args, 1500)})


def elapsed_ms(tool_context: ToolContext) -> int | None:
    t = _started.pop(tool_context.function_call_id, None) if tool_context.function_call_id else None
    return None if t is None else max(1, round((time.monotonic() - t) * 1000))


def after_tool(tool: BaseTool, args: dict, tool_context: ToolContext, tool_response: Any) -> Any:
    ms = elapsed_ms(tool_context)
    hydrator = HYDRATORS.get(tool.name)
    if hydrator is not None:
        parsed = parse_json(tool_response.get("result") if isinstance(tool_response, dict) else tool_response)
        if parsed is not None:
            hydrated = hydrator(parsed)
            emit({"type": "result", "agent": tool.name, "data": hydrated})
            emit({"type": "tool_result", "agent": tool_context.agent_name, "name": tool.name, "result": truncate(hydrated), "ms": ms})
            return hydrated
    emit({"type": "tool_result", "agent": tool_context.agent_name, "name": tool.name, "result": truncate(tool_response), "ms": ms})
    return None


def before_model(callback_context: CallbackContext, llm_request: Any) -> None:
    emit({"type": "thinking", "agent": callback_context.agent_name})


CALLBACKS = {
    "before_tool_callback": before_tool,
    "after_tool_callback": after_tool,
    "before_model_callback": before_model,
}
