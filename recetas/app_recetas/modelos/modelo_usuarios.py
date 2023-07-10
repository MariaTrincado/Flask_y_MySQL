from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas import BASE_DE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash

class Usuario:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.password = data['password']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
    
    @classmethod
    def crear_uno(cls,data):
        query = """
                INSERT INTO usuarios( nombre, apellido, correo, password )
                VALUES ( %(nombre)s, %(apellido)s, %(correo)s, %(password)s);
                """

        resultado = connectToMySQL(BASE_DE_DATOS).query_db(query,data)
        return resultado
    
    @classmethod
    def obtener_uno_mail (cls,data):
        query = """
                SELECT *
                FROM usuarios
                WHERE correo = %(correo)s;
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

        if not EMAIL_REGEX.match( data['correo'] ):
            es_valido = False
            flash ("Ingrese un correo válido",  "error_email")

        if len( data ['password'] ) < 8:
            es_valido = False
            flash ("La contraseña debe contener al menos 8 caracteres",  "error_pass")

        return es_valido
