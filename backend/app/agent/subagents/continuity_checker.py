from google.adk.agents import LlmAgent

from app.agent import trace
from app.agent.tools.clickhouse_mcp import make_clickhouse_toolset
from app.agent.tools.continuity import check_metadata
from app.agent.tools.vision import compare_frames
from app.config import settings

INSTRUCTION = """You are the ContinuityChecker. Given an ordered list of shot_ids, find continuity problems
between adjacent shots.

1. Call check_metadata once with the ordered shot_ids. It applies the archive's metadata rules
   (time of day, interior/exterior, wardrobe palette) and returns the warnings it found.
2. For every pair check_metadata flagged, and for at most 2 additional adjacent pairs of your choice,
   call compare_frames for a visual check. If compare_frames reports matches=false with severity mid or
   high on a pair that had no metadata warning, add a warning with rule "visual" and its explanation.
   If compare_frames says a flagged pair is clearly an intentional scene change (matches=true), keep the
   warning but lower its severity to low and say so in the explanation.
3. Reply with JSON only, no markdown fences:
   {"warnings": [{"pair": ["a","b"], "rule": "...", "severity": "low|mid|high", "explanation": "...",
                  "suggested_replacement": null}], "checked_pairs": <n>}
   Never drop a warning that check_metadata returned.
"""


def make_continuity_checker() -> LlmAgent:
    return LlmAgent(
        name="ContinuityChecker",
        model=settings.gemini_model,
        description="Checks an ordered shot sequence for continuity problems between adjacent shots.",
        instruction=INSTRUCTION,
        tools=[check_metadata, compare_frames, make_clickhouse_toolset(["run_query"])],
        generate_content_config=settings.fast_thinking(),
        **trace.CALLBACKS,
    )
