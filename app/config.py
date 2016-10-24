from flask import Flask
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, \
     login_required

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '123456789'

# MongoDB Config
app.config['MONGODB_DB'] = 'prueba'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

app.config['SECURITY_TRACKABLE'] = True

# Create database connection object
db = MongoEngine(app)
