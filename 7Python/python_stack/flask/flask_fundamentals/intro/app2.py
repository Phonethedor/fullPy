from flask import Flask, render_template, request

app2 = Flask(__name__)

@app2.route("/")
def estudiante():
    return render_template("estudiantes.html")

@app2.route("/resultado.html", methods=["POST","GET"])
def resultado():
    if request.method == "POST":
        resultado = request.form
        return render_template("resultado.html", resultado=resultado)

if __name__ == '__main__':
    app2.run(debug = True)