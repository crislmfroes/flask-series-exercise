from app import db

class Episodio(db.Model):
    __tablename__ = 'episodio'

    cod = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    numero = db.Column(db.Integer, db.CheckConstraint('numero > 0'))
    cod_temporada = db.Column(db.Integer, db.ForeignKey('temporada.cod'), nullable=False)