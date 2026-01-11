class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount}...")
        print("Deposit successful.")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

    def withdraw(self, amount):
        print(f"Withdrawing {amount}...")
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")


# -------- Main Program --------
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = SavingsAccount(name, balance)

# Perform operations
account.deposit(2000)
print()

account.withdraw(3000)
print()

account.show_balance()
