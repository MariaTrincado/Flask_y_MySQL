from flask import render_template, session, request, redirect, flash
from flask_bcrypt import Bcrypt
from app_recetas import app
from app_recetas.modelos.modelo_usuarios import Usuario

bcrypt = Bcrypt (app)

@app.route( '/', methods = ['GET'] )
def desplegar_log_reg():
    return render_template("log_reg.html")

@app.route('/crear/usuario', methods = ['POST'])
def nuevo_usuario():
    data = {
        **request.form
    }

    if Usuario.validar_registro( data ) == False:
        return redirect ('/')
    else:
        password_encriptado = bcrypt.generate_password_hash (data ['password'])
        data ['password'] = password_encriptado
        id_usuario = Usuario.crear_uno(data)
        session['nombre'] = data['nombre']
        session['apellido'] = data['apellido']
        session['id_usuario'] = id_usuario

        return redirect('/inicio')

@app.route('/inicio', methods = ['GET'])
def desplegar_inicio():
    if 'nombre' not in session:
        return redirect('/')
    else:
        return render_template ('inicio.html')

@app.route('/login', methods = ['POST'])
def procesa_login():
    data = {
        "correo" : request.form['email_login']
    }
    usuario = Usuario.obtener_uno_mail(data)
    if usuario == None:
        flash("Correo incorrecto, ingrese nuevamente", "error_email_login")
        return redirect('/')
    else:
        if not bcrypt.check_password_hash( usuario.password, request.form ['password_login']):
            flash ("Contraseña incorrecta, intente denuevo", "error_password_login")
            return redirect('/')
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            return redirect('/inicio')

@app.route ('/desconectar', methods = ['POST'])
def procesa_desconexion():
    session.clear()
    return redirect('/')



