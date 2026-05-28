# Testes de Caixa Preta — Equipamentos (Selenium)
# Testam o fluxo de empréstimo e devolução via navegador

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'http://127.0.0.1:5001'


def wait(driver, timeout=5):
    return WebDriverWait(driver, timeout)


def fazer_login(driver):
    """Realiza login com o usuário padrão."""
    driver.get(f'{BASE_URL}/login')
    wait(driver).until(EC.presence_of_element_located((By.ID, 'login')))
    driver.find_element(By.ID, 'login').send_keys('admin')
    driver.find_element(By.ID, 'senha').send_keys('123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    wait(driver).until(EC.url_to_be(f'{BASE_URL}/'))


# ──────────────────────────────────────────
# Testes de Visualização
# ──────────────────────────────────────────

def test_tabela_equipamentos_visivel(driver):
    """A tabela de equipamentos deve ser exibida após o login."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

    tabela = driver.find_element(By.CLASS_NAME, 'table')
    assert tabela.is_displayed()


def test_exibe_tres_equipamentos(driver):
    """Devem aparecer exatamente 3 linhas na tabela."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody tr')))

    linhas = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
    assert len(linhas) == 3


def test_todos_disponiveis_inicialmente(driver):
    """Todos os equipamentos devem ter badge verde (Disponível) no início."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-success')))

    badges_verde = driver.find_elements(By.CLASS_NAME, 'bg-success')
    assert len(badges_verde) == 3


def test_navbar_exibe_usuario_logado(driver):
    """A navbar deve exibir o nome do usuário autenticado."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar')))

    navbar = driver.find_element(By.CLASS_NAME, 'navbar')
    assert 'admin' in navbar.text.lower()


# ──────────────────────────────────────────
# Testes de Empréstimo
# ──────────────────────────────────────────

def test_pegar_equipamento_muda_badge(driver):
    """Clicar em Pegar deve alterar o badge de verde para vermelho."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))

    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-danger')))

    badges_vermelho = driver.find_elements(By.CLASS_NAME, 'bg-danger')
    assert len(badges_vermelho) == 1


def test_botao_devolver_aparece_apos_pegar(driver):
    """Após pegar, o botão deve mudar de Pegar para Devolver."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))

    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-warning')))

    botoes_devolver = driver.find_elements(By.CSS_SELECTOR, '.btn-warning')
    assert len(botoes_devolver) == 1


# ──────────────────────────────────────────
# Testes de Devolução
# ──────────────────────────────────────────

def test_devolver_equipamento_restaura_badge(driver):
    """Após devolver, o badge deve voltar para verde."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))

    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-warning')))

    driver.find_element(By.CSS_SELECTOR, '.btn-warning').click()
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-success')))

    badges_verde = driver.find_elements(By.CLASS_NAME, 'bg-success')
    assert len(badges_verde) == 3


def test_botoes_corretos_apos_multiplas_acoes(driver):
    """Após pegar 1 equipamento, deve haver 2 botões Pegar e 1 Devolver."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))

    driver.find_elements(By.CSS_SELECTOR, '.btn-primary')[0].click()
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-warning')))

    botoes_pegar = driver.find_elements(By.CSS_SELECTOR, '.btn-primary')
    botoes_devolver = driver.find_elements(By.CSS_SELECTOR, '.btn-warning')
    assert len(botoes_pegar) == 2
    assert len(botoes_devolver) == 1


# ──────────────────────────────────────────
# Testes de Persistência
# ──────────────────────────────────────────

def test_status_persiste_apos_reload(driver):
    """O status Emprestado deve persistir após recarregar a página."""
    fazer_login(driver)
    wait(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))

    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-danger')))

    driver.refresh()
    wait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

    badges_vermelho = driver.find_elements(By.CLASS_NAME, 'bg-danger')
    assert len(badges_vermelho) == 1
