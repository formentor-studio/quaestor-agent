class AccountRepositoryInMemory():
    """
    Integration with ERP
    """

    def lookup_ledger_account_for_cash(self) -> str:
        """Look up ledger account for Cash and Bank
        """
        return f"(572) Cash"

    def lookup_ledger_account_of_customer(self, name: str) -> str:
        """Look up ledger account by customer name

        Args:
            name: Name of the customer
        """

        # Steering to ask the accountant for the name of the customer
        return f"(430) Customer {name}"

    def lookup_ledger_account_for_revenue(self) -> str:
        """Look up ledger account for Sales Revenue 
        """
        return "(700) Sales/Revenue"

    def lookup_ledger_account_for_output_vat(self, vat_region: str) -> str:
        """Look up ledger account for Output VAT or Output Tax

            Args:
                name: VAT region. For example spain or canary_islands
        """
        vat_output_account_by_region = {
            "spain": "477",
            "canary_islands": "4777",
        }
        if not vat_region in vat_output_account_by_region:
            return "(477) VAT"
        
        return vat_output_account_by_region[vat_region]