# Planejamento de Testes
## Sistema de Empréstimo de Equipamentos

---

## 1. Objetivo

Este documento descreve o planejamento de testes do sistema **Sistema de Empréstimo de Equipamentos**, desenvolvido com Flask, com o objetivo de validar os fluxos funcionais da aplicação por meio de testes automatizados.

O foco do trabalho é a **qualidade e cobertura dos testes**, e não a complexidade da aplicação.

---

## 2. Escopo

### 2.1 O que será testado

| Funcionalidade | Incluído |
|---|---|
| Login com credenciais válidas | Sim |
| Login com credenciais inválidas | Sim |
| Logout | Sim |
| Acesso a rotas protegidas sem autenticação | Sim |
| Listagem de equipamentos | Sim |
| Empréstimo de equipamento | Sim |
| Devolução de equipamento | Sim |
| Persistência de dados no banco | Sim |
| Mudança visual de status (badges) | Sim |

### 2.2 O que não será testado

| Item | Motivo |
|---|---|
| Recuperação de senha | Funcionalidade não implementada |
| Múltiplos usuários simultâneos | Fora do escopo do projeto |
| Performance e carga | Fora do escopo acadêmico |
| Segurança avançada | Fora do escopo do projeto |

---

## 3. Estratégia de Testes

A estratégia combina duas abordagens complementares:

### 3.1 Caixa Branca — Pytest

Testa a lógica interna da aplicação de forma isolada, sem depender do navegador.

- **Testes Unitários**: validam os models diretamente no banco em memória
- **Testes de Integração**: validam os fluxos HTTP usando o cliente de testes do Flask

**Vantagem**: execução rápida, isolamento total, sem dependências externas.

### 3.2 Caixa Preta — Selenium

Testa a aplicação pelo ponto de vista do usuário, simulando ações reais no navegador.

- **Testes de Interface**: validam elementos visuais (badges, botões, mensagens)
- **Testes de Fluxo**: validam navegação, redirecionamentos e persistência visual

**Vantagem**: testa a experiência real do usuário, detecta erros de integração frontend/backend.

---

## 4. Ferramentas Utilizadas

| Ferramenta | Versão | Finalidade |
|---|---|---|
| Python | 3.12 | Linguagem principal |
| Flask | 3.0.3 | Framework web |
| SQLAlchemy | 3.1.1 | ORM / banco de dados |
| Flask-Login | 0.6.3 | Gerenciamento de sessão |
| SQLite | — | Banco de dados (em memória para testes) |
| pytest | 8.3.5 | Framework de testes (caixa branca) |
| Selenium | 4.21.0 | Automação de browser (caixa preta) |
| Chrome (headless) | — | Navegador para Selenium |

---

## 5. Fluxos Testados

### Fluxo 1 — Login

```
Usuário acessa /login
    → preenche login e senha
    → submete o formulário

    [credenciais corretas] → redireciona para /
    [credenciais incorretas] → exibe mensagem de erro
    [sem autenticação] → /  redireciona para /login
```

### Fluxo 2 — Empréstimo

```
Usuário autenticado acessa /
    → visualiza tabela de equipamentos
    → clica em "Pegar" (equipamento Disponível)
    → status muda para "Emprestado"
    → usuario_id salvo no banco
    → botão muda para "Devolver"
```

### Fluxo 3 — Devolução

```
Usuário autenticado acessa /
    → visualiza equipamento com status "Emprestado"
    → clica em "Devolver"
    → status volta para "Disponível"
    → usuario_id removido do banco
    → botão volta para "Pegar"
```

### Fluxo 4 — Logout

```
Usuário autenticado clica em "Sair" (navbar)
    → sessão encerrada
    → redirecionado para /login
    → acesso à / negado sem nova autenticação
```

---

## 6. Ambiente de Testes

| Item | Descrição |
|---|---|
| Sistema Operacional | Windows 10 |
| Banco de dados (pytest) | SQLite em memória (`:memory:`) |
| Banco de dados (selenium) | SQLite em arquivo temporário |
| Servidor (selenium) | Flask em thread daemon na porta 5001 |
| Navegador | Google Chrome (modo headless) |

---

## 7. Critérios de Aceite

- Todos os testes devem passar (exit code 0)
- Nenhum teste deve depender da ordem de execução
- Cada teste deve ser independente e isolado
- Screenshots devem ser gerados automaticamente em caso de falha (Selenium)
