from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_security import login_required
import config
import db
from models.User import User
from models.Role import Role

app = config.app

# Create a user to test with
@app.before_first_request
def create_user():
    if( User.objects.filter(email='matt@nobien.net').count() == 0 ):
        db.security.datastore.create_user(email='matt@nobien.net', password='password')

# Views
@app.route('/')
#@login_required
def home():
    return render_template('index.jinja2', param1 = str(app.config) )

if __name__ == '__main__':
    app.run()
