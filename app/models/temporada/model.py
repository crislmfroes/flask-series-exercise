from app import db

class Temporada(db.Model):
    __tablename__ = 'temporada'

    cod = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, db.CheckConstraint('numero > 0'))
    cod_serie = db.Column(db.Integer, db.ForeignKey('serie.cod'), nullable=False)

    episodios = db.relationship('Episodio', backref='temporada', lazy=True)

