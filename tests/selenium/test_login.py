# Testes de Caixa Preta — Login (Selenium)
# Testam o comportamento da interface via navegador

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'http://127.0.0.1:5001'


def wait(driver, timeout=5):
    return WebDriverWait(driver, timeout)


def fazer_login(driver, login='admin', senha='123'):
    """Auxilia no preenchimento e envio do formulário de login."""
    driver.get(f'{BASE_URL}/login')
    wait(driver).until(EC.presence_of_element_located((By.ID, 'login')))
    driver.find_element(By.ID, 'login').send_keys(login)
    driver.find_element(By.ID, 'senha').send_keys(senha)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


# ──────────────────────────────────────────
# Testes de Carregamento
# ──────────────────────────────────────────

def test_pagina_login_carrega(driver):
    """A página de login deve carregar e exibir os campos do formulário."""
    driver.get(f'{BASE_URL}/login')
    wait(driver).until(EC.presence_of_element_located((By.ID, 'login')))

    assert driver.find_element(By.ID, 'login').is_displayed()
    assert driver.find_element(By.ID, 'senha').is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').is_displayed()


# ──────────────────────────────────────────
# Testes de Autenticação
# ──────────────────────────────────────────

def test_login_valido(driver):
    """Login com credenciais corretas deve redirecionar para a home."""
    fazer_login(driver, 'admin', '123')
    wait(driver).until(EC.url_to_be(f'{BASE_URL}/'))

    assert driver.current_url == f'{BASE_URL}/'
    assert 'Equipamentos' in driver.page_source


def test_login_senha_invalida(driver):
    """Login com senha incorreta deve exibir mensagem de erro na tela."""
    fazer_login(driver, 'admin', 'senha_errada')
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')))

    erro = driver.find_element(By.CLASS_NAME, 'alert-danger')
    assert erro.is_displayed()
    assert 'inv' in erro.text.lower()


def test_login_usuario_inexistente(driver):
    """Login com usuário que não existe deve exibir mensagem de erro."""
    fazer_login(driver, 'usuario_fantasma', '000')
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')))

    erro = driver.find_element(By.CLASS_NAME, 'alert-danger')
    assert erro.is_displayed()


def test_login_permanece_na_pagina_apos_erro(driver):
    """Após erro de login, o usuário deve permanecer na página de login."""
    fazer_login(driver, 'admin', 'errada')
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')))

    assert 'login' in driver.current_url


# ──────────────────────────────────────────
# Testes de Sessão
# ──────────────────────────────────────────

def test_logout(driver):
    """Após logout, deve ser redirecionado para a tela de login."""
    fazer_login(driver, 'admin', '123')
    wait(driver).until(EC.url_to_be(f'{BASE_URL}/'))

    driver.get(f'{BASE_URL}/logout')
    wait(driver).until(EC.presence_of_element_located((By.ID, 'login')))

    assert 'login' in driver.current_url


def test_acesso_sem_autenticacao_redireciona(driver):
    """Acessar a home sem estar autenticado deve redirecionar para /login."""
    driver.get(f'{BASE_URL}/')
    wait(driver).until(EC.presence_of_element_located((By.ID, 'login')))

    assert 'login' in driver.current_url
