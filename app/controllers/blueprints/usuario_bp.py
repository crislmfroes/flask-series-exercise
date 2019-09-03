from flask import Blueprint, request, render_template, url_for, session
from app.forms.usuario_form import UsuarioForm
from app.forms.login_form import LoginForm
from app import db, User

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = UsuarioForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.altura = form.altura.data
        user.idade = form.idade.data
        user.login = form.login.data
        user.nome = form.nome.data
        user.set_senha(form.senha.data)
        db.session.add(user)
        db.session.commit()
        return "Ok"
    return render_template('form.html', form=form, title="Cadastro", route=url_for('usuario.cadastro'))

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and user.check_senha(form.senha.data):
            session['logado'] = True
            session['user'] = user.cod
            session['nome'] = user.nome
            return "Ok"
    return render_template('form.html', form=form, title="Login", route=url_for('usuario.login'))

@usuario_bp.route('/logout')
def logout():
    session.clear()
    return 'Ok'


