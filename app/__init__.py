from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('app')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/series_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db = SQLAlchemy(app)

from app.controllers import *
from app.models.usuario.model import User
from app.models.serie.model import Serie
from app.models.temporada.model import Temporada
from app.models.episodio.model import Episodio