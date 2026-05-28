import os
import time
import threading
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app import create_app
from models.models import db as _db, User, Equipment

BASE_URL = 'http://127.0.0.1:5001'
TEST_DB_URI = 'sqlite:///test_selenium.db'
TEST_DB_PATH = 'instance/test_selenium.db'


@pytest.fixture(scope='session')
def flask_server():
    """Inicia o servidor Flask em thread separada com banco de teste."""
    test_app = create_app({'SQLALCHEMY_DATABASE_URI': TEST_DB_URI})

    with test_app.app_context():
        _db.create_all()

        if not User.query.filter_by(login='admin').first():
            _db.session.add(User(login='admin', senha='123'))
            _db.session.commit()

        if Equipment.query.count() == 0:
            for nome in ['Notebook Dell', 'Mouse Gamer', 'Projetor Epson']:
                _db.session.add(Equipment(nome=nome, status='Disponível'))
            _db.session.commit()

    thread = threading.Thread(
        target=lambda: test_app.run(port=5001, use_reloader=False, debug=False)
    )
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Aguarda o servidor estar pronto

    yield BASE_URL

    try:
        if os.path.exists(TEST_DB_PATH):
            os.remove(TEST_DB_PATH)
    except PermissionError:
        pass  # Servidor ainda em execução na thread daemon


@pytest.fixture(scope='session')
def driver(flask_server):
    """Inicializa o Chrome WebDriver em modo headless."""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1280,800')

    # Selenium 4.6+ usa SeleniumManager para baixar o ChromeDriver automaticamente
    chrome_driver = webdriver.Chrome(options=options)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function', autouse=True)
def clean_state(driver):
    """Limpa cookies e reseta status dos equipamentos antes de cada teste."""
    driver.delete_all_cookies()

    reset_app = create_app({'SQLALCHEMY_DATABASE_URI': TEST_DB_URI})
    with reset_app.app_context():
        for eq in Equipment.query.all():
            eq.status = 'Disponível'
            eq.usuario_id = None
        _db.session.commit()

    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Salva screenshot automaticamente quando um teste falha."""
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and 'driver' in item.funcargs:
        try:
            driver = item.funcargs['driver']
            os.makedirs('tests/evidence', exist_ok=True)
            screenshot_path = f'tests/evidence/{item.name}.png'
            driver.save_screenshot(screenshot_path)
            print(f'\n[Screenshot salvo] {screenshot_path}')
        except Exception:
            pass  # Driver pode já estar fechado na fase de teardown
