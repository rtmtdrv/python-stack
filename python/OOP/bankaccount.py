
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance - 5
        self.balance -= amount

    def display_account_info(self):
        print(f"User: {self.balance}, Account Balance: ${self.balance}")

    def yield_interest(self):
        interest_gains = interest_rate * self.balance
        self.balance += interest_gains

chase = BankAccount(.13, 500)
boa = BankAccount(.16, 0)
boa.display_account_info()
chase.deposit(100)
chase.display_account_info()