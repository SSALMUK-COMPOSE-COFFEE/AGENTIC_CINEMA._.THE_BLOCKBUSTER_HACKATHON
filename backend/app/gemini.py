from functools import lru_cache

from google import genai
from google.genai import types

from app.config import settings


@lru_cache(maxsize=1)
def get_client() -> genai.Client:
    http_options = types.HttpOptions(base_url=settings.gemini_base_url) if settings.gemini_base_url else None
    return genai.Client(api_key=settings.gemini_api_key or None, http_options=http_options)
