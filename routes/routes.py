from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from models.models import db, User, Equipment

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/')
@login_required
def home():
    equipamentos = Equipment.query.all()
    return render_template('home.html', equipamentos=equipamentos)


@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form.get('login')
        senha_input = request.form.get('senha')

        user = User.query.filter_by(login=login_input, senha=senha_input).first()

        if user:
            login_user(user)
            return redirect(url_for('routes.home'))
        else:
            flash('Login ou senha inválidos.')

    return render_template('login.html')


@routes_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        login_input = request.form.get('login')
        senha_input = request.form.get('senha')

        if User.query.filter_by(login=login_input).first():
            flash('Esse login já está em uso.')
        else:
            novo_usuario = User(login=login_input, senha=senha_input)
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso! Faça login.')
            return redirect(url_for('routes.login'))

    return render_template('cadastrar.html')


@routes_bp.route('/pegar/<int:equipamento_id>')
@login_required
def pegar(equipamento_id):
    equipamento = Equipment.query.get_or_404(equipamento_id)

    if equipamento.status == 'Disponível':
        equipamento.status = 'Emprestado'
        equipamento.usuario_id = current_user.id
        db.session.commit()

    return redirect(url_for('routes.home'))


@routes_bp.route('/devolver/<int:equipamento_id>')
@login_required
def devolver(equipamento_id):
    equipamento = Equipment.query.get_or_404(equipamento_id)

    if equipamento.status == 'Emprestado':
        equipamento.status = 'Disponível'
        equipamento.usuario_id = None
        db.session.commit()

    return redirect(url_for('routes.home'))


@routes_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))
