class persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = input("Ingrese su edad: ")
    def mostrarDatos(self):
        print("Nombre :", self.nombre)
        print("Edad :", self.edad)

class trabajador (persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese su sueldo: "))
    def mostrarDatos(self):
        super().mostrarDatos()
        print("Sueldo :", self.sueldo)

    def agregarBono(self):
        if self.sueldo < 700000:
            print("El trabajador recibira bono del 10% sobre su sueldo")
        else:
            print("meh")

perso1 = persona()
perso1.mostrarDatos()
print("*" *18)
trabaja1 = trabajador()
trabaja1.mostrarDatos()
trabaja1.agregarBono()