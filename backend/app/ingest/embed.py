import asyncio
from pathlib import Path

from google.genai import types

from app.config import settings
from app.gemini import get_client

RETRIES = 8
FIRST_DELAY = 3.0
MAX_DELAY = 60.0


def _config(task_type: str) -> types.EmbedContentConfig:
    return types.EmbedContentConfig(task_type=task_type, output_dimensionality=settings.embedding_dim)


async def embed_image(image_path: Path) -> list[float]:
    client = get_client()
    part = types.Part.from_bytes(data=image_path.read_bytes(), mime_type="image/jpeg")
    delay = FIRST_DELAY
    for attempt in range(RETRIES):
        try:
            resp = await client.aio.models.embed_content(
                model=settings.embedding_model, contents=[part], config=_config("RETRIEVAL_DOCUMENT")
            )
            return list(resp.embeddings[0].values)
        except Exception:
            if attempt == RETRIES - 1:
                raise
            await asyncio.sleep(delay)
            delay = min(delay * 2, MAX_DELAY)
    raise RuntimeError("unreachable")


async def embed_text(text: str) -> list[float]:
    client = get_client()
    delay = FIRST_DELAY
    for attempt in range(RETRIES):
        try:
            resp = await client.aio.models.embed_content(
                model=settings.embedding_model, contents=text, config=_config("RETRIEVAL_QUERY")
            )
            return list(resp.embeddings[0].values)
        except Exception:
            if attempt == RETRIES - 1:
                raise
            await asyncio.sleep(delay)
            delay = min(delay * 2, MAX_DELAY)
    raise RuntimeError("unreachable")
