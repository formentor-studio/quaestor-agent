from strands import Agent
from app.agents import customer_payment
from app.util.model_provider import ModelProvider

# Get LLM model
#####
modelProvider = ModelProvider()
model_orchestrator, _ = modelProvider.get()

# Multi-Agent definition
#####

from app.agents import customer_invoice
agent = Agent(
    model=model_orchestrator,
    callback_handler=None,
    system_prompt="""
    Your job is to record journal entries from instructions using a set of accounting tools.

    ## Important Notes
    - If you do not have an accounting tool to record the journal entry just say "Unsupported transaction".
    """,
    tools=[
        customer_invoice.agent.as_tool(name="customer_invoice", description="Post journal entry for a customer invoice"),
        customer_payment.agent.as_tool(name="customer_payment", description="Post journal entry for a customer payment"),
    ],
)

request = """
Create journal entry for invoice of customer 'Joaquin' with amount 1000 euros
"""
request="""
Record purchase of 10 computers to ACME
"""
request="""
Record the invoice AB123 from customer Cervantes for $1,605
"""
request="""
Record payment of invoice AB123 from customer Cervantes for $1,605
"""
result = agent(request)

while True:
    user_input = input("\nAccountant > ").strip()
    if (user_input.lower() == "quit"):
        break
    if not user_input:
        continue
    print()
    answer = agent(user_input)
    content = answer.message.get("content", [])
    for block in content:
        if "text" in block:
            print(block["text"])

print()
print("RESULT")
print("="*6)
print(str(result))

print()
print("MESSAGES")
print("="*8)
import json
print(json.dumps(agent.messages, indent=2))
