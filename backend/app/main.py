from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.agent import router as agent_router
from app.api.films import router as films_router
from app.api.health import router as health_router
from app.api.sequences import router as sequences_router
from app.api.shots import router as shots_router
from app.config import settings

app = FastAPI(title="Shot Memory")
for r in (health_router, films_router, shots_router, sequences_router, agent_router):
    app.include_router(r, prefix="/api")

for sub in ("films", "thumbs", "proxies"):
    (settings.data_dir / sub).mkdir(parents=True, exist_ok=True)
app.mount("/media", StaticFiles(directory=settings.data_dir), name="media")
