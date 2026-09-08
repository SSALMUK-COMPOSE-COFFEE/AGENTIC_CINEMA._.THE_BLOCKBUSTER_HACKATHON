import asyncio
from pathlib import Path

from google.genai import types

from app.config import settings
from app.gemini import get_client
from app.ingest.schema import ShotMeta

PROMPT = (
    "You are a film editor's assistant logging footage. Describe this single shot for a shot log. "
    "Be concrete and visual. Do not speculate about plot beyond what is visible."
)


async def describe_shot(proxy_path: Path, retries: int = 5) -> ShotMeta:
    client = get_client()
    video = types.Part.from_bytes(data=proxy_path.read_bytes(), mime_type="video/mp4")
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=ShotMeta,
        temperature=0.2,
    )
    delay = 2.0
    for attempt in range(retries):
        try:
            resp = await client.aio.models.generate_content(
                model=settings.gemini_model, contents=[video, PROMPT], config=config
            )
            return ShotMeta.model_validate_json(resp.text)
        except Exception:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(delay)
            delay *= 2
    raise RuntimeError("unreachable")
