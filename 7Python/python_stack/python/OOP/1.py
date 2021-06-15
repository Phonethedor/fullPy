#para declarar una clase
class User:
    #para definir atributos se definir el metodo __init__ (self)
    def __init__(self, username, email_address):#se indica lo que se debe proporcionar al momento de instanciar la clase
        self.name = username
        self.email = email_address
        self.account_balance = 0
#para instanciar la clase
michael = User("Michael", "michael@codingdojo.com")
anna = User("Anna", "anna@codingdojo.com")
guido = User("Guido","guido@codingdojo.com")
monty = User("Monty", "monty@codingdojo.com")
#modificar atributos
michael.name = "Michael"
#para acceder a los atributos
print(michael.name)
print(anna.email)
