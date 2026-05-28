# Sistema de Empréstimo de Equipamentos

Projeto acadêmico desenvolvido para a disciplina de **Teste de Software**.

O foco principal não é a complexidade da aplicação, e sim a **qualidade e cobertura dos testes automatizados**, utilizando as abordagens de caixa branca (Pytest) e caixa preta (Selenium).

---

## Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.12 | Linguagem principal |
| Flask | 3.0.3 | Framework web |
| Flask-SQLAlchemy | 3.1.1 | ORM / banco de dados |
| Flask-Login | 0.6.3 | Autenticação e sessão |
| SQLite | — | Banco de dados |
| Bootstrap | 5.3.0 CDN | Interface visual |
| pytest | 8.3.5 | Testes de caixa branca |
| Selenium | 4.21.0 | Testes de caixa preta |

---

## Funcionalidades

- Login e logout com sessão gerenciada pelo Flask-Login
- Listagem de equipamentos com status visual (badge verde/vermelho)
- Empréstimo de equipamento (status → Emprestado)
- Devolução de equipamento (status → Disponível)
- Cadastro de novos usuários

---

## Estrutura do Projeto

```
P_simple/
│
├── app.py                  → ponto de entrada da aplicação
├── config.py               → configurações (banco, secret key)
├── requirements.txt        → dependências
├── pytest.ini              → configuração do pytest
├── README.md
│
├── models/
│   └── models.py           → models User e Equipment
│
├── routes/
│   └── routes.py           → todas as rotas da aplicação
│
├── templates/
│   ├── base.html           → template base com navbar
│   ├── login.html          → tela de login
│   ├── home.html           → tela principal com tabela
│   └── cadastrar.html      → tela de cadastro
│
├── static/
│   └── style.css           → estilos adicionais
│
├── tests/
│   ├── pytest/
│   │   ├── conftest.py     → fixtures (banco em memória + seed)
│   │   ├── test_unit.py    → testes unitários dos models
│   │   └── test_integration.py → testes de integração HTTP
│   │
│   ├── selenium/
│   │   ├── conftest.py     → servidor Flask + Chrome headless
│   │   ├── test_login.py   → testes de login via browser
│   │   └── test_equipment.py → testes de equipamentos via browser
│   │
│   └── evidence/           → screenshots automáticos em falhas
│
└── docs/
    ├── planejamento_testes.md
    ├── casos_de_teste.md
    ├── tabelas_decisao.md
    └── relatorio_final.md
```

---

## Instalação

**Pré-requisitos:** Python 3.10+ e Google Chrome instalados.

```bash
# Clone ou extraia o projeto
cd P_simple

# Instale as dependências
pip install -r requirements.txt
```

---

## Executar a Aplicação

```bash
python app.py
```

Acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000)

**Usuário padrão criado automaticamente:**

| Campo | Valor |
|---|---|
| Login | `admin` |
| Senha | `123` |

---

## Executar os Testes

### Todos os testes (Pytest + Selenium)

```bash
python -m pytest tests/ -v
```

### Somente testes de caixa branca (Pytest)

```bash
python -m pytest tests/pytest/ -v
```

### Somente testes de caixa preta (Selenium)

```bash
python -m pytest tests/selenium/ -v
```

### Resultado esperado

```
34 passed in ~15s
```

> Em caso de falha nos testes Selenium, screenshots são salvos automaticamente em `tests/evidence/`.

---

## Testes Implementados

### Caixa Branca — Pytest (18 testes)

| Arquivo | Quantidade | O que testa |
|---|---|---|
| `test_unit.py` | 9 | Models User e Equipment diretamente no banco |
| `test_integration.py` | 9 | Rotas HTTP completas via cliente de testes Flask |

### Caixa Preta — Selenium (16 testes)

| Arquivo | Quantidade | O que testa |
|---|---|---|
| `test_login.py` | 7 | Login, logout, acesso protegido via browser |
| `test_equipment.py` | 9 | Empréstimo, devolução, badges e persistência visual |

---

## Documentação

| Arquivo | Conteúdo |
|---|---|
| `docs/planejamento_testes.md` | Estratégia, escopo e ferramentas |
| `docs/casos_de_teste.md` | 12 casos de teste detalhados (CT-01 a CT-12) |
| `docs/tabelas_decisao.md` | Tabelas de decisão para Login, Empréstimo e Devolução |
| `docs/relatorio_final.md` | Resultados, métricas e conclusão |
