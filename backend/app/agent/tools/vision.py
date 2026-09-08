from google.genai import types
from pydantic import BaseModel

from app.config import settings
from app.db import get_client
from app.gemini import get_client as gemini_client


class ContinuityReport(BaseModel):
    matches: bool
    severity: str
    issues: list[str]
    explanation: str


PROMPT = (
    "These two frames are consecutive shots in an edited sequence. Compare them for continuity problems an "
    "editor would flag: wardrobe or prop changes on the same character, lighting direction, screen direction "
    "and eyeline (180-degree rule), time of day, weather. severity must be one of low, mid, high. "
    "If they are clearly different locations or scenes by design, report matches=true with severity low."
)


def compare_frames(shot_id_a: str, shot_id_b: str) -> dict:
    """Visually compare two shots' representative frames for continuity problems.

    Args:
        shot_id_a: first shot id in cut order.
        shot_id_b: second shot id in cut order.
    """
    rows = get_client().query(
        "SELECT shot_id, thumbnail_uri FROM shots WHERE shot_id IN %(ids)s",
        parameters={"ids": [shot_id_a, shot_id_b]},
    ).named_results()
    uris = {r["shot_id"]: r["thumbnail_uri"] for r in rows}
    parts = []
    for sid in (shot_id_a, shot_id_b):
        path = settings.data_dir / uris[sid].removeprefix("/media/")
        parts.append(types.Part.from_bytes(data=path.read_bytes(), mime_type="image/jpeg"))
    resp = gemini_client().models.generate_content(
        model=settings.gemini_model,
        contents=[*parts, PROMPT],
        config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=ContinuityReport),
    )
    report = ContinuityReport.model_validate_json(resp.text)
    return {"pair": [shot_id_a, shot_id_b], **report.model_dump()}
