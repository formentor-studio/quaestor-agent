class JournalEntryRepositoryInMemory():
    """
    Integration with ERP
    """
    
    def record(self, apuntes: list[dict], col_len: int = 50) -> str:
        self._display(apuntes=apuntes)
        
    def _display(self, apuntes: list[dict], col_len: int = 50) -> str:
        self._display_header()
        last_apunte=None
        for apunte in apuntes:
            sign = apunte["sign"]
            account = apunte["account"]
            amount = f'${apunte["amount"]}'
            if sign=="debit":
                print(f"{amount} {account}", end="")
            else:
                margin = (col_len + 5) if last_apunte["sign"] == "credit" else (col_len + 5) - len(f"{last_apunte["amount"]} {last_apunte["account"]}") -1
                print(f" "*margin, end="")
                print(f"{account}{" "*(col_len-len(str(account))-len(str(amount)))}{amount}")
            last_apunte=apunte

    def _display_header(self, col_len: int = 50):
        print("Debit", end="")
        print(" "*(col_len-len("Debit")), end="")
        print(" "*5, end="")
        print(" "*(col_len-len("Credit")), end="")
        print("Credit", end="")
        print()
        print("="*col_len, end="")
        print(" "*5,end="")
        print("="*col_len, end="")
        print()
