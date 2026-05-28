# Testes de Integração (Caixa Branca)
# Testam os fluxos HTTP completos usando o cliente de testes do Flask

from models.models import db, Equipment


# ──────────────────────────────────────────
# Testes de Login
# ──────────────────────────────────────────

def test_login_valido(client):
    """Login com credenciais corretas deve redirecionar para a home."""
    response = client.post('/login', data={'login': 'admin', 'senha': '123'}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Equipamentos' in response.data.decode('utf-8')


def test_login_senha_errada(client):
    """Login com senha incorreta deve exibir mensagem de erro."""
    response = client.post('/login', data={'login': 'admin', 'senha': 'errada'}, follow_redirects=True)
    assert 'inv' in response.data.decode('utf-8').lower()


def test_login_usuario_inexistente(client):
    """Login com usuário que não existe deve exibir mensagem de erro."""
    response = client.post('/login', data={'login': 'fantasma', 'senha': '000'}, follow_redirects=True)
    assert 'inv' in response.data.decode('utf-8').lower()


def test_acesso_sem_autenticacao_redireciona(client):
    """Acessar a home sem login deve redirecionar para /login."""
    response = client.get('/', follow_redirects=False)
    assert response.status_code == 302
    assert 'login' in response.headers['Location']


def test_logout_encerra_sessao(client):
    """Após logout, deve redirecionar para a tela de login."""
    client.post('/login', data={'login': 'admin', 'senha': '123'})
    response = client.get('/logout', follow_redirects=True)
    assert 'login' in response.data.decode('utf-8').lower()


# ──────────────────────────────────────────
# Testes de Empréstimo
# ──────────────────────────────────────────

def test_pegar_equipamento_muda_status(client):
    """Pegar um equipamento deve mudar seu status para Emprestado."""
    client.post('/login', data={'login': 'admin', 'senha': '123'})
    response = client.get('/pegar/1', follow_redirects=True)

    assert response.status_code == 200
    db.session.expire_all()
    eq = Equipment.query.filter_by(id=1).first()
    assert eq.status == 'Emprestado'


def test_devolver_equipamento_muda_status(client):
    """Devolver um equipamento deve mudar seu status para Disponível."""
    client.post('/login', data={'login': 'admin', 'senha': '123'})
    client.get('/pegar/1')
    client.get('/devolver/1')

    db.session.expire_all()
    eq = Equipment.query.filter_by(id=1).first()
    assert eq.status == 'Disponível'


def test_persistencia_usuario_no_emprestimo(client):
    """Ao pegar, o usuario_id deve ser salvo no banco."""
    client.post('/login', data={'login': 'admin', 'senha': '123'})
    client.get('/pegar/2')

    db.session.expire_all()
    eq = Equipment.query.filter_by(id=2).first()
    assert eq.status == 'Emprestado'
    assert eq.usuario_id is not None


def test_persistencia_apos_devolucao(client):
    """Após devolução, o usuario_id deve ser removido do banco."""
    client.post('/login', data={'login': 'admin', 'senha': '123'})
    client.get('/pegar/3')
    client.get('/devolver/3')

    db.session.expire_all()
    eq = Equipment.query.filter_by(id=3).first()
    assert eq.status == 'Disponível'
    assert eq.usuario_id is None
