from flask import render_template, session, request, redirect
from app_usuarios import app
from app_usuarios.modelos.modelo_usuarios import Usuarios

usuarios =[{
        "nombre" : "Peter",
        "apellido" : "Valdivia",
        "correo": "ps@gmail.com"
    },
        {
        "nombre" : "maria",
        "apellido" : "alvarez",
        "correo": "mc@gmail.com"
    }]

@app.route("/usuario", methods = ['GET'])
def obtener_usuario():
    lista_usuarios = Usuarios.seleccionar_todos()
    return render_template("leer.html", usuarios=lista_usuarios)

@app.route("/form/usuario", methods = ['GET'])
def desplegar_formulario_usuario():
    if 'nombre' in session:
        print (session['nombre'])
    else:
        session['nombre'] = 'Alexander'
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

