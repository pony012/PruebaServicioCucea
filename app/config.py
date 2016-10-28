import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, \
     login_required
import json
#
# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

app.config['PORT'] = int(os.getenv('VCAP_APP_PORT', 8080))

app.config['HOST'] = '127.0.0.1' if app.config['PORT'] == 8080 else '0.0.0.0'

app.config['DEBUG'] = True if app.config['PORT'] == 8080 else True

# # MongoDB Config
if 'VCAP_SERVICES' in os.environ:
    mongodbService = json.loads(os.environ['VCAP_SERVICES'])['mongodb'][0]
    mongodbCred = mongodbService['credentials']
    # app.config['MONGO_DB_CREDENTIALS'] = mongodbCred
    app.config['MONGODB_DB'] = str(mongodbCred['name'])
    app.config['MONGODB_HOST'] = str(mongodbCred['host'])
    app.config['MONGODB_PORT'] = int(mongodbCred['port'])
    app.config['MONGODB_USERNAME'] = str(mongodbCred['username'])
    app.config['MONGODB_PASSWORD'] = str(mongodbCred['password'])
else:
    app.config['MONGODB_DB'] = 'prueba'
    app.config['MONGODB_HOST'] = 'localhost'
    app.config['MONGODB_PORT'] = 27017
#
# app.config['SECURITY_TRACKABLE'] = True
#
# Create database connection object
db = MongoEngine(app)
