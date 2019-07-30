#!/usr/bin/env python

from app import app
from app.controllers.blueprints.usuario_bp import usuario_bp

app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run('localhost')

