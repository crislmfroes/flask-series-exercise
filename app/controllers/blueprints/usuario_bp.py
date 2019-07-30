from flask import Blueprint, request, render_template
from app.forms.usuario_form import UsuarioForm

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_bp.route('/cadastro')
def cadastro():
    form = UsuarioForm('Cadastro')
    if form.validate_on_submit():
        return "Hello World!"
    return render_template('form_usuario.html', form=form, title="Cadastro")


