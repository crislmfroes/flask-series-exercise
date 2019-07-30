from app.models.classes.usuario import Usuario
import os
import hashlib
import psycopg2
from app.models.daos.dao import Dao


class UsuarioDao(Dao):
    def __init__(self, conn_parameters, secret_key=''):
        super(UsuarioDao, self).__init__(conn_parameters, secret_key=secret_key)

    def inserir(self, usuario):
        if type(usuario) is not Usuario:
            raise ValueError()
        try:
            with psycopg2.connect(self._con_parameters) as con:
                with con.cursor() as cursor:
                    sql = "INSERT INTO Usuario(nome, login, altura, idade, email, senha) VALUES (%s, %s, %s, %s, %s, %s) RETURNING cod"
                    mogri = cursor.mogrify(sql, (
                        usuario.nome,
                        usuario.login,
                        usuario.altura,
                        usuario.idade,
                        usuario.email,
                        self._criptografar(usuario.senha)
                    ))
                    cursor.execute(mogri)
                    row = cursor.fetchone()
                    usuario.cod = row[0]
                    con.commit()
        except BaseException as e:
            print('Erro ao inserir usuario ...')
            raise e

