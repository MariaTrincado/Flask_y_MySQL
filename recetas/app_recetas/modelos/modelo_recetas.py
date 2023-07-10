from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas import BASE_DE_DATOS
from app_recetas.modelos.modelo_usuarios import Usuario
from flask import flash 

class Receta:
    def __init__(self, data) :
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.instrucciones = data['instrucciones']
        self.cuando = data['cuando']
        self.cuanto = data['cuanto']        
        self.id_usuario = data['id_usuario']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.usuario = None
        
    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO recetas (nombre, descripcion, instrucciones, cuando, cuanto, id_usuario)
                VALUES ( %(nombre)s, %(descripcion)s, %(instrucciones)s, %(cuando)s, %(cuanto)s, %(id_usuario)s)
                """
        id_receta = connectToMySQL (BASE_DE_DATOS).query_db (query, data)
        return id_receta
    
    @staticmethod
    def validar_formulario_recetas (data):
        es_valido = True
        if len(data ['nombre']) < 3:
            es_valido = False
            flash("Debes proporcionar el nombre de la receta.", "error_nombre")
        if len(data ['descripcion']) < 3:
            es_valido = False
            flash("Debes proporcionar la descripcion de la receta.", "error_descripcion")
        if len(data ['instrucciones']) < 3:
            es_valido = False
            flash("Debes proporcionar las instrucciones de la receta.", "error_instrucciones")
        if data ['cuando'] == "":
            es_valido = False
            flash("Debes proporcionar la fecha de elaboracion de la receta.", "error_cuando")
        if "cuanto" not in data:
            es_valido = False
            flash("Debes informar si la receta se elabora en menos de 30 min.", "error_cuanto")
        return es_valido
            
    @classmethod
    def obtener_todas_con_usuarios (cls,):
        query = """
                SELECT *
                FROM recetas r JOIN usuarios u
                ON  r.id_usuario = u.id                
                """
        resultado = connectToMySQL (BASE_DE_DATOS).query_db (query)
        lista_recetas = []
        for renglon in resultado:
            receta = Receta (renglon)
            data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['u.nombre'],
                "apellido" :renglon ['apellido'],
                "correo" :renglon ['correo'],
                "password" :renglon ['password'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],                    
            }
            usuario = Usuario (data_usuario)
            receta.usuario = usuario
            lista_recetas.append(receta)
        
        return lista_recetas
            
    @classmethod
    def elimina_uno (cls, data):
        query = """
                DELETE FROM recetas
                WHERE id = %(id)s ;              
                """
        return connectToMySQL(BASE_DE_DATOS).query_db(query, data)
    
    @classmethod
    def obtener_uno_con_usuario (cls, data):
        query = """
                SELECT *
                FROM recetas r JOIN usuarios u
                ON  r.id_usuario = u.id  
                WHERE r.id= %(id)s;             
                """
        resultado = connectToMySQL(BASE_DE_DATOS).query_db (query, data)
        renglon = resultado [0]
        receta = Receta (renglon)
        data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['u.nombre'],
                "apellido" :renglon ['apellido'],
                "correo" :renglon ['correo'],
                "password" :renglon ['password'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],                    
            }
        receta.usuario = Usuario (data_usuario)
        return receta
    
    @classmethod
    def editar_uno (cls, data):
        query = """
                UPDATE recetas
                SET nombre = %(nombre)s, descripcion = %(descripcion)s, instrucciones = %(instrucciones)s, cuando = %(cuando)s, cuanto = %(cuanto)s
                WHERE id= %(id)s;             
                """
        return connectToMySQL(BASE_DE_DATOS).query_db( query, data)
    
    @classmethod
    def obtener_uno (cls, data):
        query = """
                SELECT *
                FROM recetas  
                WHERE id= %(id)s;             
                """
        resultado = connectToMySQL(BASE_DE_DATOS).query_db( query, data)
        receta = Receta (resultado [0])
        return receta
    
    
                
        
    
    