from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'usuario'

    cod = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    login = db.Column(db.String(80), unique=True)
    altura = db.Column(db.Numeric)
    idade = db.Column(db.Integer)
    email = db.Column(db.String(80))
    senha = db.Column(db.String(128))

    __table_args__ = (
        db.CheckConstraint(altura > 0, name='altura_maior_que_zero'),
        db.CheckConstraint(idade > 0, name='idade_maior_que_zero'),
        {}
    )

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)

