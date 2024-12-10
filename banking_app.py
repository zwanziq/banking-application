# Base Class
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Derived Class: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest: {interest}")
        return interest

    def add_interest(self):
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Interest added. New balance: {self.balance}")

# Example Usage
if __name__ == "__main__":
    # Create a SavingsAccount object
    account = SavingsAccount(account_number=101, account_holder="John Doe", balance=5000, interest_rate=5)

    # Display account details
    account.display_account_details()

    # Deposit money
    account.deposit(1000)

    # Withdraw money
    account.withdraw(2000)

    # Calculate and add interest
    account.add_interest()

    # Final account details
    account.display_account_details()
