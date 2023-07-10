from app_login_reg.config.mysqlconnection import connectToMySQL
from app_login_reg import BASE_DE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash

class Usuario:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.tiempo_creacion = data['tiempo_creacion']
        self.tiempo_acualizacion = data['tiempo_acualizacion']
    
    @classmethod
    def crear_uno(cls,data):
        query = """
                INSERT INTO usuarios( nombre, apellido, email, password )
                VALUES ( %(nombre)s, %(apellido)s, %(email)s, %(password)s);
                """

        resultado = connectToMySQL(BASE_DE_DATOS).query_db(query,data)
        return resultado
    
    @classmethod
    def obtener_uno_mail (cls,data):
        query = """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL (BASE_DE_DATOS).query_db(query,data)

        if len(resultado)==0:
            return None
        else:
            return Usuario (resultado[0])

    @staticmethod
    def validar_registro( data ):
        es_valido = True
        if len( data['nombre'] ) < 2:
            es_valido = False
            flash ("El nombre debe contener al menos 2 caracteres", "error_nombre")

        if not NOMBRE_REGEX.match( data['nombre'] ):
            es_valido = False
            flash ("El nombre debe tener mayúscula y solo contener letras",  "error_nombre")
        
        if len( data['apellido'] ) < 2:
            es_valido = False
            flash ("El nombre debe contener al menos 2 caracteres", "error_apellido")

        if not NOMBRE_REGEX.match( data['apellido'] ):
            es_valido = False
            flash ("El apellido debe tener mayúscula y solo contener letras",  "error_apellido")

        if not EMAIL_REGEX.match( data['email'] ):
            es_valido = False
            flash ("Ingrese un correo válido",  "error_email")

        if len( data ['password'] ) < 8:
            es_valido = False
            flash ("La contraseña debe contener al menos 8 caracteres",  "error_pass")

        return es_valido
