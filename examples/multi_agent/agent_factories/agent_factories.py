"""Factory functions for building a Researcher / Coder / Reviewer agent team.

Each factory returns a fresh `Agent` instance so callers can spin up
multiple independent teams without agents sharing `agent_name` (and
therefore `persistent_memory`) with one another.
"""

from swarms import Agent


def build_researcher_agent(
    model_name: str = "gpt-5.4",
    max_loops: int = 1,
) -> Agent:
    """Build an agent that researches a task and gathers requirements."""
    return Agent(
        agent_name="Researcher",
        agent_description="Researches topics, gathers requirements, and surfaces relevant prior art.",
        system_prompt="""You are a meticulous technical researcher. Given a task, you:
    1. Identify the core requirements and constraints
    2. Research relevant approaches, libraries, and prior art
    3. Flag edge cases and open questions
    4. Summarize your findings clearly for the next person in the pipeline

    Be concise and factual. Do not write code yourself.""",
        model_name=model_name,
        max_loops=max_loops,
    )


def build_coder_agent(
    model_name: str = "gpt-5.4",
    max_loops: int = 1,
) -> Agent:
    """Build an agent that implements code from research findings."""
    return Agent(
        agent_name="Coder",
        agent_description="Implements working code based on the researcher's findings.",
        system_prompt="""You are a senior software engineer. Given research notes and
    requirements, you:
    1. Design a minimal, correct implementation
    2. Write clean, well-structured code
    3. Note any assumptions you made
    4. Call out anything the reviewer should pay close attention to

    Only output code you are confident is correct and runnable.""",
        model_name=model_name,
        max_loops=max_loops,
    )


def build_reviewer_agent(
    model_name: str = "gpt-5.4",
    max_loops: int = 1,
) -> Agent:
    """Build an agent that reviews code for correctness and quality."""
    return Agent(
        agent_name="Reviewer",
        agent_description="Reviews code for correctness, edge cases, and quality.",
        system_prompt="""You are a rigorous code reviewer. Given an implementation, you:
    1. Check correctness against the stated requirements
    2. Look for missed edge cases and bugs
    3. Flag style, readability, and maintainability issues
    4. Give a clear final verdict: approve, or request changes with specifics

    Be direct and specific in your feedback.""",
        model_name=model_name,
        max_loops=max_loops,
    )
