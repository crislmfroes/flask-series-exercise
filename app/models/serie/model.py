from app import db

class Serie(db.Model):
    __tablename__ = 'serie'

    cod = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuario.cod'), nullable=False)

    temporadas = db.relationship('temporada', backref='serie', lazy=True)