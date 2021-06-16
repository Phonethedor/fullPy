class Trabajador:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def nombre(self):
        print(self.nombre)
    def sueldo(self):
        print(self.sueldo)
    def bono(self):
        if self.sueldo > 500000:
            print('no aplica bono')
        else:
            bono = self.sueldo *0.15
            self.sueldo += bono
            print('su bono fue de:', bono)
            print('su sueldo con bono es:', self.sueldo)