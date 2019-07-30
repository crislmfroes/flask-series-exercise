from flask import Flask
import os

app = Flask('app')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '')
app.debug = True

from app.controllers import *