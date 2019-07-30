from app.models.classes.usuario import Usuario
import unittest
from hashlib import md5
import os


class UsuarioTeste(unittest.TestCase):
    def setUp(self):
        self.secret_key = os.environ.get('SECRET_KEY')
        m = md5((self.secret_key + 'qualquer coisa').encode('utf-8'))
        self.usuario1 = Usuario('Cris', 'crislmfroes', m.hexdigest())

    def testEqual(self):
        m = md5((self.secret_key + 'qualquer coisa').encode('utf-8'))
        self.assertEqual(self.usuario1.nome, 'Cris')
        self.assertEqual(self.usuario1.login, 'crislmfroes')
        self.assertEqual(self.usuario1.senha, m.hexdigest())
