class Usuario:

    def __init__(self, nome=None, login=None, senha=None):
        self.nome = nome
        self.login = login
        self.senha = senha

    def _get_nome(self):
        try:
            return self._nome
        except AttributeError:
            return None
    
    def _set_nome(self, nome):
        if type(nome) != str:
            raise ValueError()
        self._nome = nome
    
    nome = property(_get_nome, _set_nome)

    def _get_login(self):
        try:
            return self._login
        except AttributeError:
            return None
    
    def _set_login(self, login):
        if type(login) != str:
            raise ValueError()
        self._login = login
    
    login = property(_get_login, _set_login)

    def _get_altura(self):
        try:
            return self._altura
        except AttributeError:
            return None
    
    def _set_altura(self, altura):
        if type(altura) not in (float, int):
            raise ValueError()
        self._altura = altura
    
    altura = property(_get_altura, _set_altura)

    def _get_idade(self):
        try:
            return self._idade
        except AttributeError:
            return None
    
    def _set_idade(self, idade):
        if type(idade) != int:
            raise ValueError()
        self._idade = idade
    
    idade = property(_get_idade, _set_idade)

    def _get_email(self):
        try:
            return self._email
        except AttributeError:
            return None
    
    def _set_email(self, email):
        if type(email) != str:
            raise ValueError()
        self._email = email
    
    email = property(_get_email, _set_email)

    def _get_senha(self):
        try:
            return self._senha
        except AttributeError:
            return None
    
    def _set_senha(self, senha):
        if type(senha) != str:
            raise ValueError()
        self._senha = senha
    
    senha = property(_get_senha, _set_senha)

