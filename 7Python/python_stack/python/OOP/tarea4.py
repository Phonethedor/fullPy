class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate/100
        self.balance = balance
    def deposit (self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo insuficiente: cobrar una tarifa de $ 5")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print ("Saldo: $",self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            interes = self.balance * self.rate
            self.balance += interes
            return self
        else:
            print("No es posible aplicar interes a una cuenta con saldo negativo")
            return self

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=2, balance= 0)
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        return self
    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance (self):
        self.account.display_account_info
        return self
    def transfer_money (self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self