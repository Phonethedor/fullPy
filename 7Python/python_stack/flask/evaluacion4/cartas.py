from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    op = "Op loco"
    return render_template("index.html", uno = op)

#declaro objeto carta
class carta:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

#declaro objeto unidad que hereda de carta
class unidad(carta):
    def __init__(self, ataque, hp):
        super().__init__()
        self.ataque = ataque
        self.hp = hp
    def atacar(self, objetivo):
        if type(objetivo) in ('unidad'):
            objetivo.hp -= self.ataque
            if objetivo.hp <= 0:
                del objetivo
        else:
            print('El objetivo debe ser una unidad')

#declaro objeto efecto que hereda de carta
class efecto(carta):
    def __init__(self, efecto, numero):
        super().__init__()
        self.efecto = efecto
        self.numero = numero
    def usar(self, objetivo):
        if type(objetivo) in ('unidad'):
            if self.efecto in ('hp'):
                objetivo.hp == objetivo.hp + self.numero
                if objetivo.hp <= 0:
                    del objetivo
            else:
                objetivo.ataque == objetivo.ataque + self.numero
        else:
            print('El objetivo debe ser una unidad')

#declaro unidades (nombre, costo, ataque, hp)
ninjaRojo = unidad ('Ninja Cinturon Rojo', 3, 3, 4)
ninjaNegro = unidad ('Ninja Cinturon Negro', 4, 5, 4)

#declaro efectos (nombre, costo, efecto, numero)
algo = efecto('Algoritmo Duro', 2, 'hp', 3)
promesa = efecto('Promesa No Manejada', 1, 'hp', -2)
progrP = efecto('Programacion en pareja', 3, 'atk', 2)

if __name__ == '__main__':
    app.run()