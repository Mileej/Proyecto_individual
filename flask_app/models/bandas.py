from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Bandas:

    def __init__(self, data):
        self.id = data['id']
        self.genero = data['genero']
        self.nombre = data['nombre']
        self.release_date = data['release_date']
        self.comentarios = data['comentarios']
        self.pais_banda = data['pais_banda']
        self.created_at = data['created_at']
        self.estrellas = data['estrellas']
        self.user_id = data['user_id']

        #LEFT JOIN
        self.apellido = data['apellido']
    
    @staticmethod
    def valida_banda(formulario):
        es_valido = True

        if len(formulario['genero'])<2:
            # 'banda' hace  referencia a la categoria que debemos colocar en el html de new_banda
            flash('Añade un genero valido', 'banda')
            es_valido = False

        if len(formulario['nombre']) < 3:
            flash('al menos 3 caracteres', 'banda')
            es_valido = False
        
        if len(formulario['comentarios']) <10:
            flash('Al menos 10 caracteres', 'banda')
            es_valido = False

        if len(formulario['pais_banda'])<3:
            flash('Añade un  pais valido', 'banda')
            es_valido = False            

        if formulario['estrellas'] == "":
            flash('Asigne una puntuación', 'banda')
            es_valido = False

        if formulario['release_date'] == "":
            flash('Ingrese una fecha', 'banda')
            es_valido = False

        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO bandas (genero, nombre, release_date, comentarios, pais_banda, estrellas, user_id) VALUES (%(genero)s,%(nombre)s , %(release_date)s, %(comentarios)s, %(pais_banda)s, %(estrellas)s, %(user_id)s) "
        result = connectToMySQL('reseñas_musica').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT bandas.*, apellido  FROM bandas LEFT JOIN users ON users.id = bandas.user_id;"
        results = connectToMySQL('reseñas_musica').query_db(query) #Lista de diccionarios 
        bandas = []
        for banda in results:
            #recipe = diccionario
            bandas.append(cls(banda)) 

        return bandas

    @classmethod
    def get_by_id(cls, formulario):
        query= "SELECT bandas.*, apellido  FROM bandas LEFT JOIN users ON bandas.user_id=users.id  WHERE users.id =  %(id)s"
    #    query = "SELECT bandas.*, apellido  FROM bandas LEFT JOIN users ON users.id = bandas.user_id WHERE bandas.id = %(id)s"
        result = connectToMySQL('reseñas_musica').query_db(query, formulario) #Lista de diccionarios 
        banda = cls(result[0])
        return banda 

    @classmethod
    def update(cls,formulario):
        query="UPDATE bandas SET genero=%(genero)s, nombre=%(nombre)s , release_date=%(release_date)s,comentarios= %(comentarios)s, pais_banda=%(pais_banda)s,estrellas= %(estrellas)s WHERE bandas.user_id=%(id)s"
        result = connectToMySQL('reseñas_musica').query_db(query, formulario)
        return result
  
  #para eliminar
    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM bandas WHERE user_id = %(id)s"
        result = connectToMySQL('reseñas_musica').query_db(query, formulario)
        return result