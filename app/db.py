from flask_security import Security, MongoEngineUserDatastore
from config import db
from config import app
from models.User import User
from models.Role import Role
# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)
