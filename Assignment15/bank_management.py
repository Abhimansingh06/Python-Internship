"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Create a class BankAccount with:
data members (attributes) (Initialized using __init__):
    account_holder_name (str)
    current_balance (float)

Methods:
    deposit(amount): Add amount to current_balance.
    withdraw(amount): Subtract if current_balance is sufficient.
    check_balance(): Return current_balance.
    display_summary(): Print holder name and current_balance.
"""

class Bankaccount:
    def __init__(self, account_holder_name, current_balance):
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance

    def deposit(self, amount):
        self.current_balance += amount
        print(f"{amount} is deposited. New balance is {self.current_balance}")

    def withdraw(self, amount):
        if amount <= self.current_balance:
            self.current_balance -= amount
            print(f"{amount} is withdrawn. New balance is {self.current_balance}")
        else:
            print("No sufficient balance!")

    def check_balance(self):
        return self.current_balance
    
    def summary(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: {self.current_balance}")


account = Bankaccount("xyz", 5000)
account.summary()
account.deposit(1000)
account.withdraw(500)
account.check_balance()
account.summary()