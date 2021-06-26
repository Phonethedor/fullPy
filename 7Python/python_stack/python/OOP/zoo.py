class animal:
    def __init__(self):
        self.nombre = input("ingrese el nombre: ")
        self.edad = input("ingrese su edad: ")
        self.felicidad = 50
        self.hambre = 50
    def displayInfo(self):
        print("Nombre :",self.nombre)
        print("Edad :",self.edad)
        print("Felicidad :",self.felicidad)
        print("Hambre :",self.hambre)
        return self
    def alimentar(self):
        if self.felicidad == 100:
            print("No se puede aumentar mas su felicidad")
        else:
            self.felicidad += 10
            if self.felicidad > 100:
                self.felicidad = 100
        if self.hambre == 100:
            print("No se puede satisfacer mas su hambre")
        else:
            self.hambre += 10
            if self.hambre > 100:
                self.hambre = 100
        return self

class leon(animal):
    def __init__(self):
        super().__init__()
        self.peso = input("ingrese el peso: ")
        self.tipo = "Leon"
    def displayInfo(self):
        super().displayInfo()
        print("Peso :", self.peso)
        print("Tipo :", self.tipo)
    def alimentar(self):
        super().alimentar()

class tigre(animal):
    def __init__(self):
        super().__init__()
        self.peso = input("ingrese el peso: ")
        self.tipo = "Tigre"
    def displayInfo(self):
        super().displayInfo()
        print("Peso :", self.peso)
        print("Tipo :", self.tipo)
    def alimentar(self):
        super().alimentar()

class lobo(animal):
    def __init__(self):
        super().__init__()
        self.peso = input("ingrese el peso: ")
        self.tipo = "Lobo"
    def displayInfo(self):
        super().displayInfo()
        print("Peso :", self.peso)
        print("Tipo :", self.tipo)
    def alimentar(self):
        super().alimentar()

class zoo:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.animales = []
    def addLobo (self):
        self.animales.append(lobo())
        return self
    def addTigre (self):
        self.animales.append(tigre())
        return self
    def addLeon (self):
        self.animales.append(leon())
        return self
    def displayAll (self):
        print("*"*18, self.nombre, "*"*18)
        for a in range(0,len(self.animales)):
            self.animales[a].displayInfo()
        return self
    def alimentarAll(self):
        print("*"*18, self.nombre, "*"*18)
        print("*"*18, "Alimentando", "*"*18)
        for a in range(0, len(self.animales)):
            self.animales[a].alimentar()
    def agregarMasa(self):
        a = ""
        while a.upper() not in ('N', 'NO', 'S', 'SI'):
            a = ""
            b = input("ingrese el tipo de animal que desea ingresar (lobo/tigre/leon) :")
            if b.lower == "leon":
                self.animales.append(leon())
            elif b.lower == "tigre":
                self.animales.append(tigre())
            elif b.lower == "lobo":
                self.animales.append(lobo())
            else:
                print("Incorrecto")
            while a.upper() not in ('N', 'NO', 'S', 'SI'):
                a = input('¿Quieres continuar? (S/N): ')
        return self

zoo1 = zoo('zoo metropolitano')

zoo1.addLeon()
zoo1.displayAll()
zoo1.alimentarAll()
zoo1.displayAll()