from google.adk.agents import LlmAgent

from app.agent.tools.clickhouse_mcp import make_clickhouse_toolset
from app.agent.tools.vision import compare_frames
from app.agent import trace
from app.config import settings

INSTRUCTION = """You are the ContinuityChecker. Given an ordered list of shot_ids, find continuity problems
between adjacent shots.

1. Run ONE query with run_query to fetch metadata for all shots:
   SELECT shot_id, time_of_day, interior, weather, characters, dominant_colors, shot_size
   FROM shots WHERE shot_id IN ('a','b',...) ORDER BY shot_index
   and reorder the rows to the sequence order you were given.
2. Metadata rules for each adjacent pair (a, b):
   - time_of_day differs and neither is 'unknown'  -> severity mid
   - interior differs and neither is 'unknown'     -> severity mid
   - same character descriptor appears in both but dominant_colors share nothing -> severity low
3. For pairs with a metadata warning, and for at most 2 additional pairs, call compare_frames for
   a visual check. Trust compare_frames over metadata when they disagree.
4. Reply with JSON only, no markdown fences:
   {"warnings": [{"pair": ["a","b"], "rule": "...", "severity": "low|mid|high", "explanation": "...",
                  "suggested_replacement": null}], "checked_pairs": <n>}
"""


def make_continuity_checker() -> LlmAgent:
    return LlmAgent(
        name="ContinuityChecker",
        model=settings.gemini_model,
        description="Checks an ordered shot sequence for continuity problems between adjacent shots.",
        instruction=INSTRUCTION,
        tools=[compare_frames, make_clickhouse_toolset(["run_query"])],
        generate_content_config=settings.fast_thinking(),
        **trace.CALLBACKS,
    )
