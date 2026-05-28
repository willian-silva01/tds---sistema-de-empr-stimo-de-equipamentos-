# Testes Unitários (Caixa Branca)
# Testam diretamente os models — sem HTTP, sem cliente

from models.models import db, User, Equipment


# ──────────────────────────────────────────
# Testes de Usuário
# ──────────────────────────────────────────

def test_criar_usuario(app):
    """Deve criar um usuário e persistir no banco."""
    user = User(login='joao', senha='456')
    db.session.add(user)
    db.session.commit()

    assert user.id is not None
    assert user.login == 'joao'
    assert user.senha == '456'


def test_usuario_admin_existe(app):
    """O usuário admin deve existir após o seed."""
    admin = User.query.filter_by(login='admin').first()
    assert admin is not None
    assert admin.senha == '123'


def test_login_unico_no_banco(app):
    """Não deve existir dois usuários com o mesmo login."""
    total = User.query.filter_by(login='admin').count()
    assert total == 1


# ──────────────────────────────────────────
# Testes de Equipamento
# ──────────────────────────────────────────

def test_criar_equipamento(app):
    """Deve criar um equipamento e persistir no banco."""
    eq = Equipment(nome='Teclado Mecânico', status='Disponível')
    db.session.add(eq)
    db.session.commit()

    assert eq.id is not None
    assert eq.nome == 'Teclado Mecânico'
    assert eq.status == 'Disponível'


def test_status_inicial_disponivel(app):
    """Equipamentos do seed devem ter status Disponível."""
    eq = Equipment.query.filter_by(nome='Notebook Dell').first()
    assert eq.status == 'Disponível'


def test_tres_equipamentos_no_seed(app):
    """Devem existir exatamente 3 equipamentos após o seed."""
    total = Equipment.query.count()
    assert total == 3


def test_alterar_status_para_emprestado(app):
    """Deve alterar o status de Disponível para Emprestado."""
    eq = Equipment.query.filter_by(nome='Notebook Dell').first()
    eq.status = 'Emprestado'
    db.session.commit()

    atualizado = Equipment.query.filter_by(nome='Notebook Dell').first()
    assert atualizado.status == 'Emprestado'


def test_emprestimo_salva_usuario_id(app):
    """Ao emprestar, deve salvar o id do usuário responsável."""
    admin = User.query.filter_by(login='admin').first()
    eq = Equipment.query.filter_by(nome='Mouse Gamer').first()

    eq.status = 'Emprestado'
    eq.usuario_id = admin.id
    db.session.commit()

    assert eq.usuario_id == admin.id


def test_devolucao_limpa_usuario_id(app):
    """Ao devolver, deve limpar o usuario_id e restaurar status."""
    admin = User.query.filter_by(login='admin').first()
    eq = Equipment.query.filter_by(nome='Projetor Epson').first()

    # Empresta
    eq.status = 'Emprestado'
    eq.usuario_id = admin.id
    db.session.commit()

    # Devolve
    eq.status = 'Disponível'
    eq.usuario_id = None
    db.session.commit()

    resultado = Equipment.query.filter_by(nome='Projetor Epson').first()
    assert resultado.status == 'Disponível'
    assert resultado.usuario_id is None
