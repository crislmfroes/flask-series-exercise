from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, FloatField, SubmitField
from wtforms.validators import Email, EqualTo, Length, Required

class UsuarioForm(FlaskForm):
    nome = StringField("Nome", validators=[Required()])
    login = StringField("Login", validators=[Required()])
    altura = FloatField("Altura")
    idade = IntegerField("Idade")
    email = StringField("Email", validators=[Required(), Email()])
    senha = PasswordField("Senha", validators=[Required(), Length(min=8)])
    senha_confirma = PasswordField("Confirmar Senha", validators=[Required(), Length(min=8)])
    submit = SubmitField("Submeter")
