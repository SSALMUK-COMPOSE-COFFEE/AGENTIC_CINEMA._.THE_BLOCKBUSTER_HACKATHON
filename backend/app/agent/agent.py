from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from app.agent.subagents.cut_assembler import make_cut_assembler
from app.agent.subagents.librarian import make_librarian
from app.agent.subagents.narrator import make_narrator
from app.agent import trace
from app.config import settings

INSTRUCTION = """You are EditorAssistant, the front desk of a film shot archive backed by ClickHouse.

Route the editor's message:
- A description of shots to find ("rainy night, two people, close-up") -> call the Librarian tool.
- An editing brief ("build a 60-second teaser, tension rising then release") -> call the CutAssembler tool.
- A question about the archive ("how many night shots in Charade?") -> call the Librarian tool with the
  question; it can run aggregate SQL.
- Anything else -> answer briefly yourself.

The editor's screen already shows the tool result (shot grid, SQL, timeline, warnings). Never repeat the
tool JSON. After the tool returns, call the Narrator tool with a short summary of what came back (count,
the top two or three shot_ids with their captions, any warnings) and reply with the Narrator's text only."""


def make_root_agent() -> LlmAgent:
    return LlmAgent(
        name="EditorAssistant",
        model=settings.gemini_model,
        description="Front desk for shot search and rough-cut assembly.",
        instruction=INSTRUCTION,
        generate_content_config=settings.fast_thinking(),
        tools=[AgentTool(agent=make_librarian()), AgentTool(agent=make_cut_assembler()), AgentTool(agent=make_narrator())],
        **trace.CALLBACKS,
    )


root_agent = make_root_agent()
