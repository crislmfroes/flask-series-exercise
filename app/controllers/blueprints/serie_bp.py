from flask import Blueprint, request, render_template, url_for, session, redirect
from app import db, Serie, User
from app.forms.serie_form import SerieForm

serie_bp = Blueprint('serie', __name__, url_prefix='/serie')

@serie_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = SerieForm()
    if form.validate_on_submit():
        serie = Serie()
        user = User.query.get(session.get('user'))
        serie.titulo = form.titulo.data
        serie.usuario = user
        db.session.add(serie)
        db.session.commit()
        return redirect(url_for('serie.listar'))
    return render_template('form.html', form=form, title='Cadastro', route=url_for('serie.cadastro'))

@serie_bp.route('/listar')
def listar():
    series = Serie.query.filter_by(cod_usuario=session.get('user')).all()
    return render_template('lista_series.html', series=series)

@serie_bp.route('/deletar')
def deletar():
    cod = request.args.get('cod')
    Serie.query.filter_by(cod=cod).delete()
    db.session.commit()
    return redirect(url_for('serie.listar'))

