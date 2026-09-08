from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from app.agent.subagents.cut_assembler import make_cut_assembler
from app.agent.subagents.librarian import make_librarian
from app.agent.subagents.narrator import make_narrator
from app.config import settings

INSTRUCTION = """You are EditorAssistant, the front desk of a film shot archive backed by ClickHouse.

Route the editor's message:
- A description of shots to find ("rainy night, two people, close-up") -> call the Librarian tool and
  return its JSON unchanged, then add one line from the Narrator tool explaining the picks.
- An editing brief ("build a 60-second teaser, tension rising then release") -> call the CutAssembler tool
  and return its JSON unchanged, then add the Narrator's explanation.
- A question about the archive ("how many night shots in Charade?") -> call the Librarian tool with the
  question; it can run aggregate SQL.
- Anything else -> answer briefly yourself.

Always return the tool JSON first on its own line, then the explanation on following lines."""


def make_root_agent() -> LlmAgent:
    return LlmAgent(
        name="EditorAssistant",
        model=settings.gemini_model,
        description="Front desk for shot search and rough-cut assembly.",
        instruction=INSTRUCTION,
        tools=[AgentTool(agent=make_librarian()), AgentTool(agent=make_cut_assembler()), AgentTool(agent=make_narrator())],
    )


root_agent = make_root_agent()
