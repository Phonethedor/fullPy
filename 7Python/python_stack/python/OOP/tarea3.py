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

cta1 = BankAccount(1, 100)
cta2 = BankAccount(2, 200)

cta1.deposit(10).deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()

cta2.deposit(10).deposit(10).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()