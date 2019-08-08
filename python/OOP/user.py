
class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Account Balance: ${self.account_balance}")
    # def transfer_money(self, amount):
    #     self.account_balance -= amount

guido = User("Guido")
monty = User("Monty")
art = User("Art")
# art.name = "Art"


guido.make_deposit(50)
guido.make_deposit(60)
guido.make_deposit(50)
guido.make_withdrawal(100)

# print(guido.account_balance)

monty.make_deposit(10)
monty.make_deposit(15)
monty.make_withdrawal(5)
monty.make_withdrawal(3)

art.make_deposit(10)
art.make_withdrawal(5)
art.make_withdrawal(5)

guido.display_user_balance()
monty.display_user_balance()
art.display_user_balance()
