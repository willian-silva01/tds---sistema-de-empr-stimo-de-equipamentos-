# PROMPT COMPLETO — TRABALHO DE TESTE DE SOFTWARE

Você é um engenheiro de software especialista em:

* Flask
* Selenium
* Pytest
* Testes automatizados
* Testes de software acadêmicos

Seu objetivo é desenvolver COMPLETAMENTE um projeto acadêmico de Teste de Software seguindo TODOS os requisitos abaixo.

IMPORTANTE:
Este trabalho será apresentado em sala.
O foco principal NÃO é a aplicação.
O foco principal são os TESTES.

Portanto:

* a aplicação deve ser simples
* os testes devem ser completos
* a documentação deve estar excelente
* deve cobrir caixa preta e caixa branca
* deve conter tabelas de decisão
* deve conter evidências
* deve conter estrutura profissional

---

# OBJETIVO DO PROJETO

Criar uma aplicação web simples utilizando Flask para servir como base para testes automatizados.

A aplicação deve possuir pelo menos DOIS fluxos principais:

1. Login
2. Empréstimo/Devolução de equipamentos

---

# TECNOLOGIAS OBRIGATÓRIAS

Backend:

* Python
* Flask
* SQLAlchemy
* Flask-Login

Banco:

* SQLite

Testes:

* Selenium WebDriver
* Pytest

Frontend:

* HTML
* CSS
* Bootstrap CDN

---

# APLICAÇÃO

Criar um sistema extremamente simples chamado:

"Sistema de Empréstimo de Equipamentos"

---

# FUNCIONALIDADES OBRIGATÓRIAS

## 1. Login

Campos:

* login
* senha

Usuário fixo:

* admin
* senha: 123

Fluxos:

* login válido
* login inválido
* logout
* acesso protegido

---

## 2. Equipamentos

Tela inicial listando equipamentos:

* Notebook Dell
* Mouse Gamer
* Projetor Epson

Cada equipamento deve possuir:

* nome
* status

Status:

* Disponível
* Emprestado

---

## 3. Empréstimo

Botão:

* Pegar

Ação:

* muda status para Emprestado
* salva usuário responsável

---

## 4. Devolução

Botão:

* Devolver

Ação:

* muda status para Disponível
* remove usuário responsável

---

# ESTRUTURA OBRIGATÓRIA

project/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── database.db
│
├── templates/
│   ├── base.html
│   ├── login.html
│   └── home.html
│
├── static/
│   └── style.css
│
├── models/
│   └── models.py
│
├── routes/
│   └── routes.py
│
├── tests/
│   ├── selenium/
│   │   ├── test_login.py
│   │   ├── test_equipment.py
│   │   └── conftest.py
│   │
│   ├── pytest/
│   │   ├── test_unit.py
│   │   ├── test_integration.py
│   │   └── conftest.py
│   │
│   └── evidence/
│
└── docs/
├── tabelas_decisao.md
├── casos_de_teste.md
├── planejamento_testes.md
└── relatorio_final.md

---

# TESTES OBRIGATÓRIOS

# TESTES DE CAIXA PRETA — SELENIUM

Implementar Selenium WebDriver utilizando Python.

Cobrir TODOS os fluxos abaixo:

## Login

* login válido
* login inválido
* campos vazios
* logout
* acesso sem autenticação

## Equipamentos

* visualizar equipamentos
* pegar equipamento disponível
* devolver equipamento
* validar mudança de status
* validar botão correto
* validar persistência visual

## Interface

* carregamento da página
* elementos visíveis
* navegação entre páginas

IMPORTANTE:

* utilizar assertions claras
* utilizar waits quando necessário
* código organizado
* screenshots automáticos em falhas

---

# TESTES DE CAIXA BRANCA — PYTEST

Criar testes unitários e integração.

## Testes Unitários

Cobrir:

* criação de usuário
* criação de equipamento
* alteração de status
* empréstimo
* devolução

## Testes de Integração

Cobrir:

* login completo
* fluxo de empréstimo
* fluxo de devolução
* acesso protegido
* persistência no banco

IMPORTANTE:

* utilizar fixtures
* banco temporário para testes
* isolamento de testes

---

# TABELAS DE DECISÃO

Criar tabelas de decisão COMPLETAS para:

## Cenário 1 — Login

Condições:

* login correto
* senha correta
* campos preenchidos

Ações:

* permitir acesso
* negar acesso
* mostrar mensagem

---

## Cenário 2 — Empréstimo

Condições:

* equipamento disponível
* usuário autenticado

Ações:

* emprestar
* bloquear ação
* atualizar status

---

# DOCUMENTAÇÃO OBRIGATÓRIA

Gerar documentação COMPLETA em Markdown.

---

# docs/planejamento_testes.md

Deve conter:

* objetivo
* escopo
* estratégia de testes
* ferramentas utilizadas
* fluxos testados

---

# docs/casos_de_teste.md

Criar casos de teste detalhados contendo:

* ID
* objetivo
* pré-condição
* passos
* resultado esperado

---

# docs/tabelas_decisao.md

Criar tabelas organizadas e profissionais.

---

# docs/relatorio_final.md

Deve conter:

* descrição da aplicação
* descrição dos testes
* evidências
* resultados
* conclusão

---

# EVIDÊNCIAS

Gerar automaticamente:

* screenshots dos testes Selenium
* logs simples
* prints de execução

Salvar em:

tests/evidence/

---

# README.md

Deve conter:

* descrição do projeto
* tecnologias
* instalação
* execução
* execução dos testes
* estrutura do projeto

---

# REQUIREMENTS.TXT

Adicionar TODAS as dependências necessárias.

---

# EXECUÇÃO

O projeto deve funcionar com:

pip install -r requirements.txt

python app.py

pytest

---

# REGRAS IMPORTANTES

NÃO implementar:

* Docker
* JWT
* APIs complexas
* arquitetura enterprise
* React
* Vue
* microsserviços
* autenticação avançada

O projeto deve ser:

* simples
* funcional
* acadêmico
* fácil de apresentar

---

# OBJETIVO PRINCIPAL

O projeto precisa impressionar pela QUALIDADE DOS TESTES e NÃO pela complexidade da aplicação.

---

# ENTREGA FINAL

Ao finalizar:

* mostrar estrutura completa
* mostrar todos os arquivos
* garantir que nenhum requisito foi esquecido
* garantir que todos os testes executam corretamente
* garantir que o projeto está pronto para apresentação acadêmica

IMPORTANTE:
Valide antes de finalizar:

* Selenium funcionando
* Pytest funcionando
* tabelas de decisão prontas
* documentação pronta
* README pronto
* evidências geradas
* aplicação executando corretamente
