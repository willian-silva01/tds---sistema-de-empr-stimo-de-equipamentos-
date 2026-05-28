import pytest
from app import create_app
from models.models import db as _db, User, Equipment


@pytest.fixture(scope='function')
def app():
    """Cria uma instância da aplicação com banco em memória para cada teste."""
    test_app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    })

    with test_app.app_context():
        _db.create_all()

        # Seed: usuário padrão
        admin = User(login='admin', senha='123')
        _db.session.add(admin)
        _db.session.commit()

        # Seed: equipamentos padrão
        for nome in ['Notebook Dell', 'Mouse Gamer', 'Projetor Epson']:
            _db.session.add(Equipment(nome=nome, status='Disponível'))
        _db.session.commit()

        yield test_app

        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope='function')
def client(app):
    """Retorna o cliente de testes do Flask."""
    return app.test_client()
