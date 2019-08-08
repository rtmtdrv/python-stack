
class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Account Balance: ${self.account_balance}")
        return self

guido = User("Guido")
monty = User("Monty")
art = User("Art")

guido.make_deposit(50).make_deposit(60).make_deposit(50).make_withdrawal(100).display_user_balance()
monty.make_deposit(10).make_deposit(15).make_withdrawal(5).make_withdrawal(3).display_user_balance()
art.make_deposit(10).make_withdrawal(5).make_withdrawal(5).display_user_balance()
