from flask import render_template, request, redirect
from app_usuarios import app
from app_usuarios.modelos.modelo_usuarios import Usuarios

@app.route("/usuario", methods = ['GET'])
def obtener_usuario():
    lista_usuarios = Usuarios.seleccionar_todos()
    return render_template("leer.html", usuarios=lista_usuarios)

@app.route("/form/usuario", methods = ['GET'])
def desplegar_formulario_usuario():
    return render_template("crear.html")

@app.route("/nuevo/usuario", methods = ['POST'])
def agregar_usuario():
    nuevo_usuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "correo" : request.form["correo"]
    }
    Usuarios.crear_uno(nuevo_usuario)
    return redirect("/usuario")

