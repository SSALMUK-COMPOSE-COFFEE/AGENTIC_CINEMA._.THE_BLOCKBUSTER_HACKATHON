import asyncio
from pathlib import Path

from google.genai import types

from app.config import settings
from app.gemini import get_client


def _config(task_type: str) -> types.EmbedContentConfig:
    return types.EmbedContentConfig(task_type=task_type, output_dimensionality=settings.embedding_dim)


async def embed_image(image_path: Path, retries: int = 5) -> list[float]:
    client = get_client()
    part = types.Part.from_bytes(data=image_path.read_bytes(), mime_type="image/jpeg")
    delay = 2.0
    for attempt in range(retries):
        try:
            resp = await client.aio.models.embed_content(
                model=settings.embedding_model, contents=[part], config=_config("RETRIEVAL_DOCUMENT")
            )
            return list(resp.embeddings[0].values)
        except Exception:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(delay)
            delay *= 2
    raise RuntimeError("unreachable")


def embed_text(text: str) -> list[float]:
    client = get_client()
    resp = client.models.embed_content(
        model=settings.embedding_model, contents=text, config=_config("RETRIEVAL_QUERY")
    )
    return list(resp.embeddings[0].values)
