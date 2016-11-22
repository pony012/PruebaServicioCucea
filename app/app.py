# from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# from flask_mongoengine import MongoEngine
# from flask_security import login_required
from flask_security.core import UserMixin, AnonymousUser
import config
import db
from models.User import User
# from models.Role import Role

app = config.app
db_sql = config.db_sql


class Registro(db_sql.Model):
    id = db_sql.Column(db_sql.Integer, primary_key=True)
    user = db_sql.Column(db_sql.Integer, unique=False)

    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return '<Registro %r | %r>' % self.id, self.user


# Create a user to test with
@app.before_first_request
def create_user():
    if(User.objects.filter(email='matt@nobien.net').count() == 0):
        db.security.datastore.create_user(email='matt@nobien.net',
                                          password='password')


class user_role_form(FlaskForm):
    user = StringField(u'Usuario', validators=[DataRequired])
    role = StringField(u'Rol', validators=[DataRequired])
    submit = SubmitField(label="Ligar")


@app.route('/user_role/<user>/<role>')
def user_role(user, role):
    form = user_role_form()
    return render_template('user_role.jinja2', form=form, user=user, role=role)


# app.add_url_rule('/user_role/<user>/<role>', view_func=user_role)


# Views
@app.route('/')
# @login_required
def home():
    user = UserMixin
    if user.is_anonymous:
        user = AnonymousUser
    return render_template('index.jinja2', user=user)


if __name__ == '__main__':
    app.run()
