import os
import psycopg2
import hashlib

class Dao:
    def __init__(self, conn_parameters, secret_key=''):
        self._con_parameters = ''
        for parameter, value in conn_parameters.items():
            self._con_parameters = '{}={} {}'.format(
                parameter,
                value,
                self._con_parameters
            )
        self.secret_key = secret_key

    def _criptografar(self, string):
        return hashlib.md5((self.secret_key + string).encode('utf-8')).hexdigest()

