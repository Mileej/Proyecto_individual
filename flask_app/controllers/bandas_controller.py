from flask import render_template, redirect, session, request, flash
from flask_app import app


#Importación del modelo
from flask_app.models.users import User
from flask_app.models.bandas import Bandas


@app.route('/new/banda')
def new_banda():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    return render_template('new_banda.html', user=user)


@app.route('/create/banda', methods=['POST'])
def create_banda():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Bandas.valida_banda(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/new/banda')

    Bandas.save(request.form)

    return redirect('/bandas')

@app.route('/edit/banda/<int:id>') #a través de la URL recibimos el ID de banda
def edit_banda(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia de lo que queremos editar
    formulario_banda = {"id": id}
    banda = Bandas.get_by_id(formulario_banda)

    return render_template('edit_banda.html', user=user, banda=banda)

@app.route('/update/banda', methods=['POST'])
def update_banda():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    
    if not Bandas.valida_banda(request.form): #llama a la función de valida_banda enviándole el formulario, comprueba que sea valido 
        return redirect('/edit/banda/'+request.form['id'])
    
    Bandas.update(request.form)
    return redirect('/bandas')

@app.route('/view/banda/<int:id>') #A través de la URL recibimos el ID de la receta
def view_banda(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


    formulario_banda = { "id": id }
    #llamar a una función y debo de recibir la receta
    banda = Bandas.get_by_id(formulario_banda)

    return render_template('view.html', user=user, banda=banda)

#Ahora para eliminar 

@app.route('/delete/banda/<int:id>')
def delete_banda(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Bandas.delete(formulario)

    return redirect('/bandas')