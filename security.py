from flask_security import Security, MongoEngineUserDatastore, \
     login_required
from app.config import app, db
from app.models.User import User
from app.models.Role import Role

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)
