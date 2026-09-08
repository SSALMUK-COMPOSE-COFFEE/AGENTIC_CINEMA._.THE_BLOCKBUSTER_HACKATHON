from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.health import router as health_router
from app.config import settings

app = FastAPI(title="Shot Memory")
app.include_router(health_router, prefix="/api")

settings.data_dir.mkdir(parents=True, exist_ok=True)
for sub in ("thumbs", "proxies"):
    (settings.data_dir / sub).mkdir(exist_ok=True)
app.mount("/media", StaticFiles(directory=settings.data_dir), name="media")
