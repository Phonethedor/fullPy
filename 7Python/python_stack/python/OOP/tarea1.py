class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount
    def make_withdrawal (self, amount):
        self.account_balance -= amount
    def display_user_balance (self):
        print("$"+str(self.account_balance))
    def transfer_money (self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
    
michael = User("Michael", "michael@codingdojo.com")
anna = User("Anna", "anna@codingdojo.com")
guido = User("Guido","guido@codingdojo.com")

michael.make_deposit(10)
michael.make_deposit(10)
michael.make_deposit(10)
michael.make_withdrawal(5)
michael.display_user_balance()

anna.make_deposit(10)
anna.make_deposit(10)
anna.make_withdrawal(5)
anna.make_withdrawal(5)
anna.display_user_balance()

guido.make_deposit(100)
guido.make_withdrawal(10)
guido.make_withdrawal(10)
guido.make_withdrawal(10)
guido.display_user_balance()

michael.transfer_money(guido,20)
michael.display_user_balance()
guido.display_user_balance()