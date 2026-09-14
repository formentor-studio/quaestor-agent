from strands_evals import Case, Experiment, eval_task
from strands_evals.evaluators import TrajectoryEvaluator
from app.agents import customer_invoice
from strands_evals.extractors import tools_use_extractor
from strands_evals.tools.evaluation_tools import any_order_match_scorer

@eval_task() 
def get_response_with_tools(case: Case) -> dict:
    """Run agent and capture tool trajectory."""
    agent = customer_invoice.agent

    response = agent(case.input)

    # Extract the tool call trajectory
    trajectory = tools_use_extractor.extract_agent_tools_used_from_messages(agent.messages)

    return {"output": str(response), "trajectory": trajectory}

# Define cases with expected tool sequences
test_cases = [
    Case[str, str](
        name="customer_invoice",
        input="Record the invoice AB123 from customer Cervantes for $1,605",
        expected_trajectory=["lookup_ledger_account_of_customer", "lookup_ledger_account_for_revenue", "lookup_ledger_account_for_output_vat", "post_journal_entry_for_customer_invoice"],
        metadata={"category": "workflow_compliance"},
    ),
]

# Create trajectory evaluator
from strands.models.ollama import OllamaModel
evaluator = TrajectoryEvaluator(
    model="us.amazon.nova-lite-v1:0",
    rubric="""
    - Use any_order_match_scorer: the expected tools should appear and order does not matter.
    - Score 1.0 if the expected sequence is followed correctly.
    - Score 0.5 if it is called extra tools.
    - Score 0.0 if expected tools are missing entirely.
    """,
    include_inputs=True,
    tools=[any_order_match_scorer]
)

# Run experiment
experiment = Experiment[str, str](cases=test_cases, evaluators=[evaluator])
output = experiment.run_evaluations(get_response_with_tools)

print(output)