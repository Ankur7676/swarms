"""Multi-agent collaboration example built on the agent_factories module.

Chains a Researcher, a Coder, and a Reviewer into a SequentialWorkflow:
the researcher's findings feed the coder, and the coder's implementation
feeds the reviewer for a final verdict.
"""

from swarms import SequentialWorkflow

from agent_factories import (
    build_coder_agent,
    build_researcher_agent,
    build_reviewer_agent,
)

researcher = build_researcher_agent()
coder = build_coder_agent()
reviewer = build_reviewer_agent()

workflow = SequentialWorkflow(
    name="research-code-review-pipeline",
    agents=[researcher, coder, reviewer],
    max_loops=1,
)

if __name__ == "__main__":
    result = workflow.run(
        "Build a Python function that validates email addresses using a regex."
    )
    print(result)
