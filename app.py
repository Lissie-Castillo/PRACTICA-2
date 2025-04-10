from flask import Flask

app = Flask(__name__)

@app.route("/")
def salu():
    return "Hola"

@app.route("/que_tal/<Nombre>/<Apellido>")
def saludar(Nombre, Apellido):
   
    return "Hola " + Nombre+ " " + Apellido
