from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from app.agent import trace
from app.agent.subagents.continuity_checker import make_continuity_checker
from app.agent.subagents.librarian import make_librarian
from app.agent.tools.edl import build_edl, save_sequence
from app.config import settings

INSTRUCTION = """You are the CutAssembler. You turn an editing brief into an ordered shot sequence.

1. Parse the brief: target length in seconds, structure (e.g. tension rising to a climax then release),
   tone, must-include elements. Only restrict to a film if the editor names one.
2. Split the structure into 3 or 4 beats. For each beat decide a tension range (1-5), a shot size
   (wide early, close at the peak), and a short visual description.
3. For each beat call the Librarian tool ONCE with a request such as
   "tension 4-5, close-ups, two people confronting, limit 6". Always ask for limit 6.
   Never call the Librarian more than 4 times in total.
4. Pick shots so beat durations add up to roughly the target length (use t_out - t_in). Prefer shots with
   consecutive shot_index values from the same film inside a beat. Never reuse a shot_id.
5. Call ContinuityChecker once with the ordered shot_ids. For every warning with severity mid or high,
   swap the second shot of the pair for another candidate you already have from the same beat. Do not
   recheck.
6. Call build_edl with the final shot_ids, then save_sequence with the brief text and the shot_ids.
7. Reply with JSON only, no markdown fences, and do not copy the timeline or EDL text back:
   {"brief": "...", "beats": [{"name": "...", "shot_ids": [...]}], "shot_ids": [...],
    "warnings": <warnings list from ContinuityChecker>, "sequence_id": "<id from save_sequence>"}
"""


def make_cut_assembler() -> LlmAgent:
    return LlmAgent(
        name="CutAssembler",
        model=settings.gemini_model,
        description="Assembles an ordered shot sequence and EDL from an editing brief.",
        instruction=INSTRUCTION,
        tools=[AgentTool(agent=make_librarian()), AgentTool(agent=make_continuity_checker()), build_edl, save_sequence],
        generate_content_config=settings.fast_thinking(),
        **trace.CALLBACKS,
    )
