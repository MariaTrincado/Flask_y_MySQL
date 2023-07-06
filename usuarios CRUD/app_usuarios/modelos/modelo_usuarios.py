from app_usuarios.config.mysqlconnection import connectToMySQL
from app_usuarios import BASE_DE_DATOS

class Usuarios:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.tiempo_creacion = data['tiempo_creacion']
        self.tiempo_acualizacion = data['tiempo_acualizacion']

    @classmethod
    def seleccionar_todos( cls ):
        query = """
                SELECT * 
                FROM usuarios;
                """

        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query )
        lista_usuarios = []
        for renglon in resultado:
            lista_usuarios.append( Usuarios( renglon ) )
        return lista_usuarios
    
    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO usuarios( nombre, apellido, correo )
                VALUES ( %(nombre)s, %(apellido)s, %(correo)s );
                """

        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )

        return resultado
    
    @classmethod
    def elimina_uno (cls, data ):
        query = """
            DELETE FROM usuarios 
            WHERE id = %(id)s;
            """
        return connectToMySQL (BASE_DE_DATOS).query_db(query, data)
    
    @classmethod
    def selecciona_uno( cls, data ):
        query = """
                SELECT *
                FROM usuarios
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        usuario_actual = Usuarios( resultado[0] )
        return usuario_actual
    
    @classmethod
    def actualiza_uno( cls, data ):
        query = """
                UPDATE usuarios
                SET nombre = %(nombre)s, apellido = %(apellido)s, correo = %(correo)s
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db( query, data )


