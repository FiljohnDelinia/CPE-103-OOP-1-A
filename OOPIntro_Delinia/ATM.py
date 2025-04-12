class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transaction_summary = []  # to track transactions

    def deposit(self, account, amount):
        account.current_balance += amount
        print("Deposit Complete")
        self.transaction_summary.append(
            f"Deposited {amount} to {account.account_firstname} {account.account_lastname} (Acct#: {account.account_number})"
        )

    def withdraw(self, account, amount):
        account.current_balance -= amount
        print("Withdraw Complete")
        self.transaction_summary.append(
            f"Withdrew {amount} from {account.account_firstname} {account.account_lastname} (Acct#: {account.account_number})"
        )

    def check_currentbalance(self, account):
        print(f"Current Balance: {account.current_balance}")

    def view_transactionsummary(self):
        print("\n--- Transaction Summary ---")
        if not self.transaction_summary:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_summary:
                print(transaction)
