from google.adk.agents import LlmAgent

from app.config import settings

INSTRUCTION = """You are the Narrator. You explain the archive team's results to a film editor in plain,
professional language: why these shots match, what alternatives exist, what the continuity warnings mean
and how to resolve them. Keep it under 120 words. Never invent shots that were not returned."""


def make_narrator() -> LlmAgent:
    return LlmAgent(
        name="Narrator",
        model=settings.gemini_model,
        description="Explains search and assembly results to the editor.",
        instruction=INSTRUCTION,
    )
