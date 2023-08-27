from flask import Flask, request,render_template,session

app = Flask(__name__)
app.secret_key ="miLlaveSecreta"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/home")
def home():
    return render_template("inicio.html")

@app.route("/mision")
def mision():
    return render_template("mision.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/servicios")
def servicios():
    return render_template("servicio.html")

@app.route("/ingresar")
def ingresar():
    return render_template("inicioSecion.html")

@app.route("/iniciarSecion",methods=["POST"])
def iniciarSecion():
    usuario= request.form["txtUsuario"]
    contraseña= request.form["txtPassword"]
    try:
        if (usuario=="admin" and contraseña=="admin"):
            session["user"]="admin"
            return render_template("administrador/inicio.html")
        elif (usuario=="asis" and contraseña=="asis"):
            session["user"]="asis"
            return render_template("asistente/inicio.html")
        else:
            return render_template("iniciarSecion.html", mensaje="Credenciales no Validas")
    except Exception as error:
        mensaje=error

@app.route("/inicioAdmin")
def inicioAdmin():
    return render_template("administrador/inicio.html")

@app.route("/inicioAsis")
def inicioAsis():
    return render_template("asistente/inicio.html")

@app.route("/salir")
def salir():
    session.clear()
    return render_template("inicioSecion.html",mensaje="Ha cerrado secion")

@app.route("/administrador")
def inicioAdministrador():
    if "admin" in session:
        return render_template("administrador/inicio.html")
    else:
        return render_template("inicioSecion.html", mensaje="Debe Primero Iniciar Secion")   
if __name__=="__main__":
    app.run(port=3000,debug=True)