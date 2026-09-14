from strands import tool

from erp.account_repository_in_memory import AccountRepositoryInMemory
from erp.journal_entry_repository_in_memory import JournalEntryRepositoryInMemory

accountRepositoryInMemory = AccountRepositoryInMemory()
journalEntryRepositoryInMemory = JournalEntryRepositoryInMemory()

# Tools to get ledger account
#####
@tool
def lookup_ledger_account_for_cash() -> str:
    """Look up ledger account for Cash and Bank
    """
    return accountRepositoryInMemory.lookup_ledger_account_for_cash()

@tool
def lookup_ledger_account_of_customer(name: str) -> str:
    """Look up ledger account by customer name

    Args:
        name: Name of the customer
    """

    return accountRepositoryInMemory.lookup_ledger_account_of_customer(name=name)

@tool
def lookup_ledger_account_for_revenue() -> str:
    """Look up ledger account for Sales Revenue 
    """
    return accountRepositoryInMemory.lookup_ledger_account_for_revenue()

@tool
def lookup_ledger_account_for_output_vat(vat_region: str) -> str:
    """Look up ledger account for Output VAT or Output Tax

        Args:
            name: VAT region. For example spain or canary_islands
    """
    return accountRepositoryInMemory.lookup_ledger_account_for_output_vat(vat_region=vat_region)

# Tools to record journal entries
#####
@tool
def post_journal_entry_for_customer_invoice(
    customer_account: str,
    revenue_account: str,
    vat_account: str,
    invoice_amount: float,
    ) -> str:
    """Post journal entry for a customer invoice

    Args:
        customer_account: Ledger account of the customer.
        revenue_account: Ledger account for sales and revenue.
        vat_account: Ledger account for Output VAT.
        invoice_amount: Amount of the invoice.
    """
    vat_amount=round(invoice_amount*0.21, 2)
    revenue_amount=invoice_amount-vat_amount

    journalEntryRepositoryInMemory.record(apuntes=[
        {
            "sign":"debit",
            "account":customer_account,
            "amount":invoice_amount, 
        },
        {
            "sign":"credit",
            "account":revenue_account,
            "amount":revenue_amount, 
        },
        {
            "sign":"credit",
            "account":vat_account,
            "amount":vat_amount, 
        },
    ])

    return f"journal entry posted successfully"

@tool
def post_journal_entry_for_customer_payment(
    customer_account: str,
    cash_account: str,
    payment_amount: float,
    ) -> str:
    """Post journal entry for a customer payment

    Args:
        customer_account: Ledger account of the customer.
        cash_account: Ledger account for for Cash and Bank.
        payment_amount: Payment amount.
    """

    journalEntryRepositoryInMemory.record(apuntes=[
        {
            "sign":"debit",
            "account":cash_account,
            "amount":payment_amount, 
        },
        {
            "sign":"credit",
            "account":customer_account,
            "amount":payment_amount, 
        }
    ])

    return f"journal entry posted successfully"
