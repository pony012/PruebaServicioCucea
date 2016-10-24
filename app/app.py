from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, \
     login_required
import config
import security
from models.User import User
from models.Role import Role

app = config.app

# Create a user to test with
@app.before_first_request
def create_user():
    print User
    if( User.objects.filter(email='matt@nobien.net').count() == 0 ):
        security.user_datastore.create_user(email='matt@nobien.net', password='password')

@app.template_filter('exception')
def my_exception_filter(value):
    try:
        return value
    except:
        return 'E:'
# Views
@app.route('/')
@login_required
def home():
    cantidadUsuarios = User.objects.filter(email='matt@nobien.net').count()
    return render_template('index.jinja2', Usuarios = User, param2 = cantidadUsuarios)

# if __name__ == '__main__':
#     app.run()
