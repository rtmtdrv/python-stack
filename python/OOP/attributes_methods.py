class User:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount

# guido = User()
# monty = User()

# guido.name = "Guido"
# monty.name = "Monty"

# print(guido.name)
# print(monty.name)

guido = User("Guido")
monty = User("Monty")


guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(100)
monty.make_deposit(50)

print(guido.account_balance)
print(monty.account_balance)


