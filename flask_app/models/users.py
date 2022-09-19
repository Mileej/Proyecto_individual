from flask_app.config.mysqlconnection import  connectToMySQL

import re #Importando Expresiones regulares,
# que consten en una regla de caracteres para crear un patron que se cumpla o no dentro de las condicionales
#es como un patron
#Expresion Regular de Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash # flash nos permite desplegar mensajes de error en el usuario

class User:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, formulario):
        #lo que esta en azul es lo que se recibe del formulario
        query = "INSERT INTO users (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s)"
        result = connectToMySQL('reseñas_musica').query_db(query, formulario) #me regresan el nuevo ID de la persona registrada
        return result

    @staticmethod
    def valida_usuario(formulario):
        #Validar los campos

        es_valido = True
        #Validar que todos los campos son requeridos 
        
        #Validar que el nombre tenga al menos 2 caracteres
        if len(formulario['nombre']) < 2 :
            flash('El nombre debe de tener al menos 2 caracteres', 'registro')
            es_valido = False
        
        if len(formulario['apellido']) < 2:
            flash('El apellido debe de tener al menos 2 caracteres', 'registro')
            es_valido = False

        #Verificar que el email tenga formato correcto - EXPRESIONES REGULARES
        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail inválido', 'registro')
            es_valido = False
        
        #Password con al menos 6 caracteres, lo dejaremos con 6 por que no se especifica cuanto es el minimo
        if len(formulario['password']) < 6:
            flash('Contraseña debe tener al menos 6 caracteres', 'registro')
            es_valido = False
        
        #Verificamos que las contraseñas coincidan
        if formulario['password'] != formulario['confirm_password']:
            flash('Las contraseñas no coinciden', 'registro')
            es_valido = False
        
        #Consultar si ya existe ese correo electrónico
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('reseñas_musica').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False
        
        return es_valido


    @classmethod
    def get_by_email(cls, formulario):
        #formulario = {
        #      email: elena@cd.com
        #      password: 123
        #}
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('reseñas_musica').query_db(query, formulario) #Los SELECT regresan una lista
        if len(result) < 1: #NO existe registro con ese correo
            #result = []
            return False
        else:
            #result = [
            #    {id: 1, first_name: elena, last_name:de troya.....} -> POSICION 0
            #]
            user = cls(result[0])  #User({id: 1, first_name: elena, last_name:de troya.....})
            return user
    
    @classmethod
    def get_by_id(cls, formulario):
        #formulario = {id: 4}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('reseñas_musica').query_db(query, formulario) #RECIBIMOS UNA LISTA
        user = cls(result[0]) #creamos una instancia de usuario
        return user