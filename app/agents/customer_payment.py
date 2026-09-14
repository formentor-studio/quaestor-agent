from strands import Agent
from app.ledger_tools import (
    lookup_ledger_account_of_customer, 
    lookup_ledger_account_for_cash, 
    post_journal_entry_for_customer_payment
)

# Get LLM model
#####
from app.util.model_provider import ModelProvider
modelProvider = ModelProvider()
_, model_journal_entry = modelProvider.get()

# Agent definition
#####
agent = Agent(
    name="customer-invoice",
    description="Post journal entry for a customer payment",
    model=model_journal_entry,
    callback_handler=None,
    system_prompt="""
    Post journal entries for customer payment.

    1. Look up ledger account for cash using `lookup_ledger_account_for_cash`.
    2. Look up ledger account for the customer using `lookup_ledger_account_of_customer`.
    4. Post journal entry for customer invoice using `post_journal_entry_for_customer_payment` with required ledger accounts and payment amount.

    ## Important Notes
    - Never post a journal entry if you do not know the required ledger accounts.
    """,
    tools=[lookup_ledger_account_of_customer, lookup_ledger_account_for_cash, post_journal_entry_for_customer_payment],
)
