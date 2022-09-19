from flask_app import app

#Importando mi controlador
from flask_app.controllers import  users_controller, bandas_controller
# siempre debemos instalar lo siguiente: 

#pipenv install flask pymysql flask-bcrypt
#pipenv shell
#python server.py -> python3 py python

if __name__=="__main__":
    app.run(debug=True) 