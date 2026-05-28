# Casos de Teste
## Sistema de Empréstimo de Equipamentos

---

## Módulo 1 — Login

---

### CT-01 — Login com credenciais válidas

| Campo | Descrição |
|---|---|
| **ID** | CT-01 |
| **Objetivo** | Verificar que o sistema autentica corretamente um usuário com credenciais válidas |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Usuário `admin` com senha `123` cadastrado no banco |

**Passos:**
1. Acessar `/login`
2. Preencher o campo **Login** com `admin`
3. Preencher o campo **Senha** com `123`
4. Clicar em **Entrar**

**Resultado esperado:** Redirecionamento para `/` com a tabela de equipamentos visível.

**Arquivo de teste:** `test_integration.py::test_login_valido` / `test_login.py::test_login_valido`

---

### CT-02 — Login com senha incorreta

| Campo | Descrição |
|---|---|
| **ID** | CT-02 |
| **Objetivo** | Verificar que o sistema rejeita credenciais inválidas e exibe mensagem de erro |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Usuário `admin` cadastrado no banco |

**Passos:**
1. Acessar `/login`
2. Preencher o campo **Login** com `admin`
3. Preencher o campo **Senha** com `senha_errada`
4. Clicar em **Entrar**

**Resultado esperado:** Permanecer em `/login` com mensagem de erro contendo "inválidos".

**Arquivo de teste:** `test_integration.py::test_login_senha_errada` / `test_login.py::test_login_senha_invalida`

---

### CT-03 — Login com usuário inexistente

| Campo | Descrição |
|---|---|
| **ID** | CT-03 |
| **Objetivo** | Verificar que o sistema rejeita usuários não cadastrados |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Nenhum usuário com login `fantasma` cadastrado |

**Passos:**
1. Acessar `/login`
2. Preencher o campo **Login** com `fantasma`
3. Preencher o campo **Senha** com `000`
4. Clicar em **Entrar**

**Resultado esperado:** Permanecer em `/login` com mensagem de erro.

**Arquivo de teste:** `test_integration.py::test_login_usuario_inexistente` / `test_login.py::test_login_usuario_inexistente`

---

### CT-04 — Acesso sem autenticação

| Campo | Descrição |
|---|---|
| **ID** | CT-04 |
| **Objetivo** | Verificar que rotas protegidas redirecionam para login quando o usuário não está autenticado |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Nenhuma sessão ativa |

**Passos:**
1. Acessar `/` diretamente sem realizar login

**Resultado esperado:** Redirecionamento (HTTP 302) para `/login`.

**Arquivo de teste:** `test_integration.py::test_acesso_sem_autenticacao_redireciona` / `test_login.py::test_acesso_sem_autenticacao_redireciona`

---

### CT-05 — Logout

| Campo | Descrição |
|---|---|
| **ID** | CT-05 |
| **Objetivo** | Verificar que o logout encerra a sessão corretamente |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Usuário autenticado como `admin` |

**Passos:**
1. Realizar login com `admin` / `123`
2. Acessar `/logout` (ou clicar em "Sair" na navbar)

**Resultado esperado:** Redirecionamento para `/login`. Novo acesso a `/` deve redirecionar novamente para `/login`.

**Arquivo de teste:** `test_integration.py::test_logout_encerra_sessao` / `test_login.py::test_logout`

---

## Módulo 2 — Equipamentos

---

### CT-06 — Listagem de equipamentos

| Campo | Descrição |
|---|---|
| **ID** | CT-06 |
| **Objetivo** | Verificar que a tela inicial exibe os 3 equipamentos cadastrados |
| **Tipo** | Caixa Preta |
| **Pré-condição** | Usuário autenticado; 3 equipamentos no banco com status `Disponível` |

**Passos:**
1. Realizar login
2. Acessar `/`

**Resultado esperado:** Tabela exibindo 3 linhas: Notebook Dell, Mouse Gamer, Projetor Epson. Todos com badge verde (Disponível) e botão "Pegar".

**Arquivo de teste:** `test_equipment.py::test_exibe_tres_equipamentos`

---

### CT-07 — Empréstimo de equipamento

| Campo | Descrição |
|---|---|
| **ID** | CT-07 |
| **Objetivo** | Verificar que clicar em "Pegar" altera o status do equipamento para Emprestado |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Usuário autenticado; equipamento com status `Disponível` |

**Passos:**
1. Realizar login
2. Clicar em **Pegar** no primeiro equipamento da lista

**Resultado esperado:**
- Status muda para `Emprestado` no banco
- Badge vermelho exibido na tela
- Botão muda para "Devolver"
- `usuario_id` salvo no banco

**Arquivo de teste:** `test_integration.py::test_pegar_equipamento_muda_status` / `test_equipment.py::test_pegar_equipamento_muda_badge`

---

### CT-08 — Devolução de equipamento

| Campo | Descrição |
|---|---|
| **ID** | CT-08 |
| **Objetivo** | Verificar que clicar em "Devolver" restaura o status para Disponível |
| **Tipo** | Caixa Preta / Integração |
| **Pré-condição** | Usuário autenticado; equipamento com status `Emprestado` |

**Passos:**
1. Realizar login
2. Clicar em **Pegar** em um equipamento
3. Clicar em **Devolver** no mesmo equipamento

**Resultado esperado:**
- Status volta para `Disponível` no banco
- Badge verde exibido na tela
- Botão volta para "Pegar"
- `usuario_id` removido (None) no banco

**Arquivo de teste:** `test_integration.py::test_devolver_equipamento_muda_status` / `test_equipment.py::test_devolver_equipamento_restaura_badge`

---

### CT-09 — Persistência do status no banco

| Campo | Descrição |
|---|---|
| **ID** | CT-09 |
| **Objetivo** | Verificar que o status persiste no banco após o empréstimo |
| **Tipo** | Integração |
| **Pré-condição** | Usuário autenticado; equipamento disponível |

**Passos:**
1. Realizar login
2. Acessar `/pegar/2`
3. Consultar o banco diretamente

**Resultado esperado:** `Equipment.status == 'Emprestado'` e `Equipment.usuario_id is not None`.

**Arquivo de teste:** `test_integration.py::test_persistencia_usuario_no_emprestimo`

---

### CT-10 — Persistência visual após reload

| Campo | Descrição |
|---|---|
| **ID** | CT-10 |
| **Objetivo** | Verificar que o status persiste visualmente após recarregar a página |
| **Tipo** | Caixa Preta |
| **Pré-condição** | Usuário autenticado; equipamento emprestado |

**Passos:**
1. Realizar login
2. Clicar em **Pegar** em um equipamento
3. Recarregar a página (F5)

**Resultado esperado:** O badge vermelho (Emprestado) permanece visível após o reload.

**Arquivo de teste:** `test_equipment.py::test_status_persiste_apos_reload`

---

## Módulo 3 — Unitários (Models)

---

### CT-11 — Criação de usuário

| Campo | Descrição |
|---|---|
| **ID** | CT-11 |
| **Objetivo** | Verificar que o model User é persistido corretamente no banco |
| **Tipo** | Unitário |
| **Pré-condição** | Banco em memória inicializado |

**Passos:**
1. Instanciar `User(login='joao', senha='456')`
2. Adicionar à sessão e fazer commit

**Resultado esperado:** `user.id` é gerado automaticamente; `user.login == 'joao'`.

**Arquivo de teste:** `test_unit.py::test_criar_usuario`

---

### CT-12 — Criação de equipamento

| Campo | Descrição |
|---|---|
| **ID** | CT-12 |
| **Objetivo** | Verificar que o model Equipment é persistido corretamente no banco |
| **Tipo** | Unitário |
| **Pré-condição** | Banco em memória inicializado |

**Passos:**
1. Instanciar `Equipment(nome='Teclado Mecânico', status='Disponível')`
2. Adicionar à sessão e fazer commit

**Resultado esperado:** `eq.id` gerado; `eq.status == 'Disponível'`.

**Arquivo de teste:** `test_unit.py::test_criar_equipamento`
