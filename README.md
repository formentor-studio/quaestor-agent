# quaestor-agent
AI agent that creates and records journal entries to an ERP from natural-language requests.

## Prerequisites
- Python 3.10+

## Setup
```
git clone https://github.com/formentor-studio/quaestor-agent.git
cd quaestor-agent

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage
1. Start conversation with **quaestor**
```
python3 quaestor.py
```

2. Request quaestor to record customer invoice:

**Accountant >** `Record the invoice AB123 from customer Cervantes for $1,605`

3. Request quaestor to record customer payment:

**Accountant >** `Record payment of invoice AB123 from customer Cervantes for $1,605`

> 🛑 It is implemented just transactions `customer invoices` and `customer payments`

## How it works
It's been defined a Multi-Agent applying the strategy `Orchestrator control`.

By transaction type it is implemented a Sub-agent provided with `tools` to get ledger accounts from ERP and to record journal entries in the ERP
> 👉🏻 sub-agents just have the necessary tools for the specific transaction

From accounting instructions the Agent orchestrator resolves the transaction type and calls the sub-agent specialised in this task.

## Project structure
```
├── app
│   ├── agents                   
│   │   ├── customer_invoice.py                # Sub-Agent that records customer invoices
│   │   └── customer_payment.py                # Sub-Agent that records customer payments
│   ├── ledger_tools.py                        # Tools to look up accounts and record transactions in ERP
│   └── util
│       └── model_provider.py
├── erp
│   ├── account_repository_in_memory.py        # Integration with ERP to look up accounts
│   └── journal_entry_repository_in_memory.py  # Integration with ERP to record transaccions
├── quaestor.py                                # Agent (the orchestrator)
└── quaestor_eval.py                           # Evaluation of orchestrator 
```
