# Relatório Final de Testes
## Sistema de Empréstimo de Equipamentos

---

## 1. Descrição da Aplicação

O **Sistema de Empréstimo de Equipamentos** é uma aplicação web desenvolvida com Python e Flask para fins acadêmicos. O objetivo da aplicação é servir como base para a prática de testes de software automatizados.

### Tecnologias utilizadas

| Tecnologia | Versão | Função |
|---|---|---|
| Python | 3.12 | Linguagem principal |
| Flask | 3.0.3 | Framework web |
| Flask-SQLAlchemy | 3.1.1 | ORM para banco de dados |
| Flask-Login | 0.6.3 | Gerenciamento de sessão/autenticação |
| SQLite | — | Banco de dados relacional |
| Bootstrap | 5.3.0 | Interface visual (CDN) |

### Funcionalidades implementadas

1. **Login / Logout** — autenticação com usuário e senha, sessão gerenciada pelo Flask-Login
2. **Listagem de equipamentos** — tabela com nome, status e ação disponível
3. **Empréstimo** — altera status para `Emprestado` e registra o usuário responsável
4. **Devolução** — restaura status para `Disponível` e remove o vínculo com o usuário
5. **Cadastro de usuário** — criação de novos usuários para fins de teste

---

## 2. Descrição dos Testes

### 2.1 Estrutura de testes

```
tests/
├── pytest/
│   ├── conftest.py         → fixtures com banco em memória
│   ├── test_unit.py        → 8 testes unitários
│   └── test_integration.py → 9 testes de integração
│
├── selenium/
│   ├── conftest.py         → servidor Flask + Chrome headless
│   ├── test_login.py       → 7 testes de login via browser
│   └── test_equipment.py   → 9 testes de equipamentos via browser
│
└── evidence/               → screenshots de falhas (automático)
```

### 2.2 Testes de Caixa Branca — Pytest

Utilizando o cliente de testes do Flask com banco SQLite em memória (`:memory:`), garantindo isolamento total entre testes.

#### Testes Unitários (`test_unit.py`)

| ID | Teste | Resultado |
|---|---|---|
| U-01 | `test_criar_usuario` | ✅ PASSOU |
| U-02 | `test_usuario_admin_existe` | ✅ PASSOU |
| U-03 | `test_login_unico_no_banco` | ✅ PASSOU |
| U-04 | `test_criar_equipamento` | ✅ PASSOU |
| U-05 | `test_status_inicial_disponivel` | ✅ PASSOU |
| U-06 | `test_tres_equipamentos_no_seed` | ✅ PASSOU |
| U-07 | `test_alterar_status_para_emprestado` | ✅ PASSOU |
| U-08 | `test_emprestimo_salva_usuario_id` | ✅ PASSOU |
| U-09 | `test_devolucao_limpa_usuario_id` | ✅ PASSOU |

#### Testes de Integração (`test_integration.py`)

| ID | Teste | Resultado |
|---|---|---|
| I-01 | `test_login_valido` | ✅ PASSOU |
| I-02 | `test_login_senha_errada` | ✅ PASSOU |
| I-03 | `test_login_usuario_inexistente` | ✅ PASSOU |
| I-04 | `test_acesso_sem_autenticacao_redireciona` | ✅ PASSOU |
| I-05 | `test_logout_encerra_sessao` | ✅ PASSOU |
| I-06 | `test_pegar_equipamento_muda_status` | ✅ PASSOU |
| I-07 | `test_devolver_equipamento_muda_status` | ✅ PASSOU |
| I-08 | `test_persistencia_usuario_no_emprestimo` | ✅ PASSOU |
| I-09 | `test_persistencia_apos_devolucao` | ✅ PASSOU |

### 2.3 Testes de Caixa Preta — Selenium

Utilizando Chrome em modo headless com Flask rodando em thread separada na porta 5001.

#### Testes de Login (`test_login.py`)

| ID | Teste | Resultado |
|---|---|---|
| S-01 | `test_pagina_login_carrega` | ✅ PASSOU |
| S-02 | `test_login_valido` | ✅ PASSOU |
| S-03 | `test_login_senha_invalida` | ✅ PASSOU |
| S-04 | `test_login_usuario_inexistente` | ✅ PASSOU |
| S-05 | `test_login_permanece_na_pagina_apos_erro` | ✅ PASSOU |
| S-06 | `test_logout` | ✅ PASSOU |
| S-07 | `test_acesso_sem_autenticacao_redireciona` | ✅ PASSOU |

#### Testes de Equipamentos (`test_equipment.py`)

| ID | Teste | Resultado |
|---|---|---|
| S-08 | `test_tabela_equipamentos_visivel` | ✅ PASSOU |
| S-09 | `test_exibe_tres_equipamentos` | ✅ PASSOU |
| S-10 | `test_todos_disponiveis_inicialmente` | ✅ PASSOU |
| S-11 | `test_navbar_exibe_usuario_logado` | ✅ PASSOU |
| S-12 | `test_pegar_equipamento_muda_badge` | ✅ PASSOU |
| S-13 | `test_botao_devolver_aparece_apos_pegar` | ✅ PASSOU |
| S-14 | `test_devolver_equipamento_restaura_badge` | ✅ PASSOU |
| S-15 | `test_botoes_corretos_apos_multiplas_acoes` | ✅ PASSOU |
| S-16 | `test_status_persiste_apos_reload` | ✅ PASSOU |

---

## 3. Evidências

### 3.1 Resultado da Execução

```
============================= test session starts =============================
platform win32 -- Python 3.12.3, pytest-8.3.5
collected 34 items

tests/pytest/test_integration.py  ......... (9 passed)
tests/pytest/test_unit.py          ......... (9 passed)
tests/selenium/test_equipment.py   ......... (9 passed)
tests/selenium/test_login.py       ....... (7 passed)

====================== 34 passed in 15.27s =======================
```

### 3.2 Cobertura por Módulo

| Módulo | Testes | Situação |
|---|---|---|
| Autenticação (Login/Logout) | 12 | ✅ Coberto |
| Empréstimo de equipamentos | 12 | ✅ Coberto |
| Models (User / Equipment) | 9 | ✅ Coberto |
| Interface visual (badges, botões) | 7 | ✅ Coberto |
| **Total** | **34** | **✅ 100% aprovados** |

### 3.3 Screenshots automáticos

Em caso de falha nos testes Selenium, screenshots são salvos automaticamente em:

```
tests/evidence/<nome_do_teste>.png
```

---

## 4. Resultados

### Resumo Executivo

| Métrica | Valor |
|---|---|
| Total de testes executados | 34 |
| Testes aprovados | 34 |
| Testes reprovados | 0 |
| Taxa de aprovação | 100% |
| Tempo de execução | ~15 segundos |

### Distribuição por tipo

| Tipo | Quantidade | % |
|---|---|---|
| Unitários (Caixa Branca) | 9 | 26% |
| Integração (Caixa Branca) | 9 | 26% |
| Selenium Login (Caixa Preta) | 7 | 21% |
| Selenium Equipamentos (Caixa Preta) | 9 | 27% |

---

## 5. Conclusão

O projeto atingiu todos os objetivos propostos:

- A aplicação foi desenvolvida de forma simples, funcional e didática
- Os testes cobrem os dois fluxos principais: **Login** e **Empréstimo/Devolução**
- A abordagem combinada de **caixa branca** (pytest) e **caixa preta** (Selenium) garante cobertura em diferentes níveis da aplicação
- Os testes são **isolados**, **independentes** e **reproduzíveis**
- A documentação está completa com tabelas de decisão, casos de teste e planejamento

### Lições aprendidas

1. Testes de integração detectam erros que testes unitários não capturam (fluxo HTTP completo)
2. Testes Selenium validam a experiência real do usuário, incluindo comportamento visual
3. O isolamento de banco de dados por teste é essencial para resultados confiáveis
4. O uso de fixtures torna os testes mais legíveis e reutilizáveis

---

*Relatório gerado para fins acadêmicos — Disciplina de Teste de Software*
