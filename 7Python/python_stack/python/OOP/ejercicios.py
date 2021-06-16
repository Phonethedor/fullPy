class Trabajador:
    def __init__(self):
        self.nombre = input("ingrese su nombre: ")
        self.sueldo = int(input("Ingrese su sueldo: "))
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)
    def bono(self):
        if self.sueldo > 500000:
            print('no aplica bono')
        else:
            bono = self.sueldo *0.15
            self.sueldo += bono
            print('su bono fue de:', bono)
            print('su sueldo con bono es:', self.sueldo)

trabajador = Trabajador()
trabajador.imprimir()
trabajador.bono()