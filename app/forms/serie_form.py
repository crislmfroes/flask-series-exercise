from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SerieForm(FlaskForm):
    titulo = StringField("Título")
    submit = SubmitField("Submeter")