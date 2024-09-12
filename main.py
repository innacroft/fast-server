from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
#    print("Detalles de la solicitud:")
#    print("Método:", request.method)
#    print("URL:", request.url)
#    print("Datos de formulario:", request.form)
#    print("Datos de consulta:", request.args)
     print("Datos JSON:", request.json)
#    print("Cabeceras:", request.headers)
#     print(request.json)
     return "ok"
