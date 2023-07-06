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

@app.route( "/eliminar/usuario/<int:id>", methods=["POST"] )
def elimina_usuario( id ):
    data = {
        "id" : id
    }
    Usuarios.elimina_uno( data )
    return redirect( "/usuario" )

@app.route( "/formulario/usuario/<int:id>", methods=["GET"] )
def desplegar_formulario_editar_usuario( id ):
    data = {
        "id" : id
    }
    usuario_actual = Usuarios.selecciona_uno( data )
    return render_template( "editar.html", usuario_actual = usuario_actual )

@app.route("/actualizar/usuario/<int:id>", methods=["POST"])
def actualiza_usuario(id):
    data = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "correo": request.form["correo"]
    }
    Usuarios.actualiza_uno(data)
    return redirect("/usuario")

@app.route("/ver/usuario/<int:id>", methods=["GET"])
def ver_usuario(id):
    data = {
        "id": id
    }
    usuario_actual = Usuarios.selecciona_uno(data)
    return render_template("ver.html", usuario_actual=usuario_actual)
