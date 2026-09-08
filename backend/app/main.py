import asyncio
import contextlib
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.agent.runner import stream_chat
from app.api.agent import router as agent_router
from app.api.films import router as films_router
from app.api.health import router as health_router
from app.api.sequences import router as sequences_router
from app.api.shots import router as shots_router
from app.config import settings


async def warm_up() -> None:
    with contextlib.suppress(Exception):
        async for _ in stream_chat("system", "warm-up", "Reply with the single word ready."):
            pass


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    task = asyncio.create_task(warm_up())
    yield
    task.cancel()


app = FastAPI(title="Shot Memory", lifespan=lifespan)
for r in (health_router, films_router, shots_router, sequences_router, agent_router):
    app.include_router(r, prefix="/api")

for sub in ("films", "thumbs", "proxies"):
    (settings.data_dir / sub).mkdir(parents=True, exist_ok=True)
app.mount("/media", StaticFiles(directory=settings.data_dir), name="media")
