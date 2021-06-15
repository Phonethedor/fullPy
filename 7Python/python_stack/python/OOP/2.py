class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
    	self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

guido = User("Guido","guido@codingdojo.com")
monty = User("Monty", "monty@codingdojo.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.account_balance)
print(monty.account_balance)