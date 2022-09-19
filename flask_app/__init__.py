#inicializar la aplicaciones

from flask import Flask

app = Flask(__name__)

#Establecemos una secret key
app.secret_key = "Mi llave super secreta"