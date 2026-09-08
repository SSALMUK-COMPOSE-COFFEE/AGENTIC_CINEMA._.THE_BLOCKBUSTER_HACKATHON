from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from app.agent.subagents.continuity_checker import make_continuity_checker
from app.agent.subagents.librarian import make_librarian
from app.agent.tools.edl import build_edl, save_sequence
from app.config import settings

INSTRUCTION = """You are the CutAssembler. You turn an editing brief into an ordered shot sequence.

1. Parse the brief: target length in seconds, structure (e.g. tension rising to a climax then release),
   tone, must-include elements, film restrictions.
2. Split the structure into 3 to 5 beats. For each beat decide a tension range (1-5), a shot-size
   progression (wide to close as tension rises), and a visual description.
3. For each beat call the Librarian tool once with a request such as
   "night exterior, tension 4-5, close-ups, two people confronting, limit 8".
   The Librarian returns JSON with a "shots" list.
4. Pick shots so beat durations add up to the target length. Prefer consecutive shot_index values from
   the same film inside a beat. Never reuse a shot_id.
5. Call ContinuityChecker with the ordered shot_ids. For every warning with severity mid or high, replace
   the second shot of the pair with the next best candidate from the same beat, then recheck once.
6. Call build_edl with the final shot_ids, then save_sequence with the session id from state
   (key 'session_id') and the brief text.
7. Reply with JSON only:
   {"brief": "...", "beats": [{"name": "...", "shot_ids": [...]}], "shot_ids": [...],
    "timeline": <timeline from build_edl>, "edl": "<edl text>", "total_seconds": <n>,
    "warnings": <warnings from ContinuityChecker>, "sequence_id": "<id>"}
"""


def make_cut_assembler() -> LlmAgent:
    return LlmAgent(
        name="CutAssembler",
        model=settings.gemini_model,
        description="Assembles an ordered shot sequence and EDL from an editing brief.",
        instruction=INSTRUCTION,
        tools=[AgentTool(agent=make_librarian()), AgentTool(agent=make_continuity_checker()), build_edl, save_sequence],
    )
