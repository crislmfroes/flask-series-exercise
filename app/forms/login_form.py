from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    login = StringField('Login')
    senha = PasswordField('Senha')
    submit = SubmitField('Submeter')
