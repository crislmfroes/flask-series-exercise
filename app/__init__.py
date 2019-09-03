from flask import Flask, session, redirect, url_for, request
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

@app.before_request
def filtra_logado():
    if session.get('logado') != True and request.endpoint not in ('usuario.login', 'usuario.cadastro'):
        return redirect(url_for('usuario.login'))

@app.before_first_request
def cria_bd():
    db.create_all()
