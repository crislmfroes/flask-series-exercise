from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, FloatField, SubmitField
from wtforms.validators import Email, EqualTo, Length, DataRequired, ValidationError

class UsuarioForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    login = StringField("Login", validators=[DataRequired()])
    altura = FloatField("Altura")
    idade = IntegerField("Idade")
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])
    senha_confirma = PasswordField("Confirmar Senha", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Submeter")

    def validate_senha(self, senha):
        if senha.data != self.senha_confirma.data:
            raise ValidationError("Both passwords must match.")
