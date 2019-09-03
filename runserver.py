#!/usr/bin/env python

from app import app
from app.controllers.blueprints.usuario_bp import usuario_bp
from app.controllers.blueprints.serie_bp import serie_bp

app.register_blueprint(usuario_bp)
app.register_blueprint(serie_bp)

if __name__ == '__main__':
    app.run('localhost')

