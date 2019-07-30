from app.models.daos.usuario_dao import Usuario, UsuarioDao
import unittest
import os

class UsuarioDaoTeste(unittest.TestCase):
    def setUp(self):
        self.secret_key = os.environ.get('SECRET_KEY')
        self.conn_parameters = {
            'dbname': 'series_db',
            'user': 'postgres'
        }
        self.usuario_dao = UsuarioDao(self.conn_parameters, secret_key=self.secret_key)
        self.usuario1 = Usuario('Cris', 'crislmfroes', 'qualquer coisa')

    def testInsert(self):
        self.usuario_dao.inserir(self.usuario1)
        self.assertNotEqual(self.usuario1.cod, None)

