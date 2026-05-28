# PROMPT_DESENVOLVIMENTO.md

# Sistema de Empréstimo de Equipamentos — Projeto Flask

## Objetivo

Criar um sistema extremamente simples utilizando Flask apenas para fins acadêmicos de testes de software.

O foco principal do projeto NÃO é a complexidade do sistema, e sim:

* testes automatizados
* validações
* cenários de teste
* estrutura mínima funcional

O sistema deve ser pequeno, simples e fácil de entender.

---

# Regras Gerais do Projeto

* Utilizar Python com Flask
* Utilizar SQLite
* Utilizar SQLAlchemy
* Utilizar Flask-Login
* Código simples e didático
* Não utilizar arquitetura complexa
* Não utilizar microsserviços
* Não utilizar Docker
* Não utilizar JWT
* Não utilizar APIs REST avançadas
* Não implementar funcionalidades desnecessárias

IMPORTANTE:
Desenvolver em etapas.
NÃO fazer tudo de uma vez.

---

# Etapa 1 — Estrutura Inicial do Projeto

Crie um projeto simples em Flask chamado:

```txt
Sistema de Empréstimo de Equipamentos
```

Estrutura desejada:

```txt
project/
│
├── app.py
├── config.py
├── requirements.txt
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
└── routes/
    └── routes.py
```

Nesta etapa:

* criar estrutura de pastas
* configurar Flask
* configurar banco SQLite
* configurar SQLAlchemy
* configurar Flask-Login
* criar model User
* criar model Equipment
* criar app.py funcional

## Model User

Campos:

* id
* login
* senha

## Model Equipment

Campos:

* id
* nome
* status
* usuario_id

Status possíveis:

* Disponível
* Emprestado

No final:

* mostrar todos os arquivos completos
* mostrar requirements.txt
* mostrar como executar o projeto

NÃO criar:

* testes
* dashboard avançado
* APIs
* Docker
* autenticação complexa

---

# Etapa 2 — Implementar Login

Agora implemente SOMENTE o sistema de login.

Regras:

* manter simplicidade máxima
* usar Flask-Login
* sem registro de usuários
* criar usuário fixo diretamente no banco
* sem criptografia de senha
* foco didático

Implementar:

* rota /login
* rota /logout
* proteção de rota usando @login_required
* sessão de usuário

## Tela login.html

Campos:

* login
* senha
* botão entrar
* mensagens de erro simples

Fluxo:

* login correto → redireciona para home
* login incorreto → mostra mensagem

Criar:

* usuário admin
* senha 123

NÃO implementar:

* cadastro
* recuperação de senha
* níveis de acesso
* JWT
* API

No final:

* mostrar arquivos modificados completos
* mostrar como testar login

---

# Etapa 3 — Tela Inicial e Listagem

Agora implemente SOMENTE a tela inicial.

Objetivo:
listar equipamentos cadastrados no banco.

Implementar:

* rota /
* listagem simples em tabela HTML

## Colunas

* Nome
* Status
* Ação

## Ação

* se disponível → botão “Pegar”
* se emprestado → botão “Devolver”

Visual:

* utilizar Bootstrap CDN
* interface extremamente simples

Adicionar:

* 3 equipamentos fictícios automaticamente no banco

Exemplo:

* Notebook Dell
* Mouse Gamer
* Projetor Epson

NÃO implementar:

* histórico
* paginação
* filtros
* dashboard
* gráficos

No final:

* mostrar arquivos completos alterados
* mostrar como visualizar no navegador

---

# Etapa 4 — Implementar Empréstimo e Devolução

Agora implemente SOMENTE a lógica de empréstimo e devolução.

Regras:

* sistema extremamente simples
* sem histórico
* sem logs

Implementar:

* rota para pegar equipamento
* rota para devolver equipamento

## Ao pegar

* status → Emprestado
* salvar usuario_id

## Ao devolver

* status → Disponível
* limpar usuario_id

## Regras

* equipamento disponível pode ser emprestado
* equipamento emprestado pode ser devolvido

Após ação:

* redirecionar para home

NÃO implementar:

* validações complexas
* múltiplos usuários simultâneos
* auditoria
* histórico
* confirmação modal

No final:

* mostrar apenas arquivos modificados completos
* explicar fluxo das rotas

---

# Etapa 5 — Melhorias Visuais Simples

Agora implemente apenas melhorias visuais mínimas.

Adicionar:

* navbar simples
* nome do usuário logado
* botão logout
* badges coloridas para status

## Status

* Disponível → verde
* Emprestado → vermelho

Manter:

* Bootstrap CDN
* simplicidade máxima

NÃO implementar:

* dark mode
* animações
* responsividade avançada
* templates complexos

No final:

* mostrar apenas arquivos modificados

---

# Etapa 6 — Estrutura de Testes

Agora implemente SOMENTE a estrutura de testes automatizados.

Utilizar:

* pytest

Criar:

```txt
tests/
│
├── test_login.py
├── test_routes.py
└── conftest.py
```

Implementar testes:

* login válido
* login inválido
* acesso sem autenticação
* empréstimo de equipamento
* devolução de equipamento

Objetivo:

* testes simples
* foco acadêmico
* fácil entendimento

NÃO implementar:

* mocks complexos
* cobertura avançada
* testes assíncronos

No final:

* mostrar arquivos completos
* mostrar como executar pytest

---

# Etapa 7 — Documentação Final

Agora gere SOMENTE a documentação final do projeto.

Criar:

* README.md

Conteúdo:

* descrição do projeto
* tecnologias utilizadas
* estrutura de pastas
* como instalar
* como executar
* como rodar testes
* funcionalidades
* screenshots fictícios opcionais

Objetivo:

* documentação simples
* padrão GitHub
* fácil apresentação acadêmica

NÃO adicionar:

* arquitetura enterprise
* microsserviços
* DevOps
* CI/CD
* Docker
* Kubernetes
