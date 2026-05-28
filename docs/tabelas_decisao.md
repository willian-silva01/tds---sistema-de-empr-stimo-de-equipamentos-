# Tabelas de Decisão
## Sistema de Empréstimo de Equipamentos

> As tabelas de decisão mapeiam combinações de condições de entrada e as ações resultantes esperadas pelo sistema.

---

## Tabela 1 — Login

### Condições de Entrada

| # | Condição |
|---|---|
| C1 | Login preenchido |
| C2 | Senha preenchida |
| C3 | Login existe no banco |
| C4 | Senha corresponde ao login |

### Ações Resultantes

| # | Ação |
|---|---|
| A1 | Redirecionar para a home (`/`) |
| A2 | Exibir mensagem de erro |
| A3 | Permanecer na tela de login |

### Tabela de Decisão

| Regra | R1 | R2 | R3 | R4 | R5 |
|---|:---:|:---:|:---:|:---:|:---:|
| **C1** Login preenchido | ✅ | ✅ | ✅ | ✅ | ❌ |
| **C2** Senha preenchida | ✅ | ✅ | ✅ | ❌ | — |
| **C3** Login existe no banco | ✅ | ✅ | ❌ | — | — |
| **C4** Senha corresponde | ✅ | ❌ | — | — | — |
| **A1** Redirecionar para home | ✅ | ❌ | ❌ | ❌ | ❌ |
| **A2** Exibir mensagem de erro | ❌ | ✅ | ✅ | ✅ | — |
| **A3** Permanecer no login | ❌ | ✅ | ✅ | ✅ | ✅ |

### Descrição das Regras

| Regra | Cenário | Resultado |
|---|---|---|
| R1 | Login e senha corretos | Acesso permitido → home |
| R2 | Login correto, senha errada | Acesso negado → mensagem de erro |
| R3 | Usuário não existe no banco | Acesso negado → mensagem de erro |
| R4 | Login preenchido, senha vazia | Bloqueado pelo HTML5 (campo `required`) |
| R5 | Login vazio | Bloqueado pelo HTML5 (campo `required`) |

### Casos de Teste Relacionados

| Regra | Caso de Teste |
|---|---|
| R1 | CT-01 |
| R2 | CT-02 |
| R3 | CT-03 |
| R4 | CT-02 (variação) |
| R5 | CT-02 (variação) |

---

## Tabela 2 — Empréstimo de Equipamento

### Condições de Entrada

| # | Condição |
|---|---|
| C1 | Usuário autenticado |
| C2 | Equipamento existe no banco |
| C3 | Status do equipamento é `Disponível` |

### Ações Resultantes

| # | Ação |
|---|---|
| A1 | Mudar status para `Emprestado` |
| A2 | Salvar `usuario_id` no banco |
| A3 | Redirecionar para home |
| A4 | Nenhuma alteração no banco |
| A5 | Redirecionar para login |

### Tabela de Decisão

| Regra | R1 | R2 | R3 | R4 |
|---|:---:|:---:|:---:|:---:|
| **C1** Usuário autenticado | ✅ | ✅ | ✅ | ❌ |
| **C2** Equipamento existe | ✅ | ✅ | ❌ | — |
| **C3** Status é `Disponível` | ✅ | ❌ | — | — |
| **A1** Status → `Emprestado` | ✅ | ❌ | ❌ | ❌ |
| **A2** Salvar `usuario_id` | ✅ | ❌ | ❌ | ❌ |
| **A3** Redirecionar para home | ✅ | ✅ | ❌ | ❌ |
| **A4** Nenhuma alteração | ❌ | ✅ | ✅ | ❌ |
| **A5** Redirecionar para login | ❌ | ❌ | ❌ | ✅ |

### Descrição das Regras

| Regra | Cenário | Resultado |
|---|---|---|
| R1 | Usuário logado, equipamento disponível | Empréstimo realizado com sucesso |
| R2 | Usuário logado, equipamento já emprestado | Nenhuma alteração, retorna para home |
| R3 | Equipamento não existe (ID inválido) | Erro 404 |
| R4 | Usuário não autenticado | Redireciona para login |

### Casos de Teste Relacionados

| Regra | Caso de Teste |
|---|---|
| R1 | CT-07, CT-09 |
| R2 | CT-07 (variação) |
| R4 | CT-04 |

---

## Tabela 3 — Devolução de Equipamento

### Condições de Entrada

| # | Condição |
|---|---|
| C1 | Usuário autenticado |
| C2 | Equipamento existe no banco |
| C3 | Status do equipamento é `Emprestado` |

### Ações Resultantes

| # | Ação |
|---|---|
| A1 | Mudar status para `Disponível` |
| A2 | Remover `usuario_id` (None) |
| A3 | Redirecionar para home |
| A4 | Nenhuma alteração no banco |
| A5 | Redirecionar para login |

### Tabela de Decisão

| Regra | R1 | R2 | R3 | R4 |
|---|:---:|:---:|:---:|:---:|
| **C1** Usuário autenticado | ✅ | ✅ | ✅ | ❌ |
| **C2** Equipamento existe | ✅ | ✅ | ❌ | — |
| **C3** Status é `Emprestado` | ✅ | ❌ | — | — |
| **A1** Status → `Disponível` | ✅ | ❌ | ❌ | ❌ |
| **A2** Remover `usuario_id` | ✅ | ❌ | ❌ | ❌ |
| **A3** Redirecionar para home | ✅ | ✅ | ❌ | ❌ |
| **A4** Nenhuma alteração | ❌ | ✅ | ✅ | ❌ |
| **A5** Redirecionar para login | ❌ | ❌ | ❌ | ✅ |

### Descrição das Regras

| Regra | Cenário | Resultado |
|---|---|---|
| R1 | Usuário logado, equipamento emprestado | Devolução realizada com sucesso |
| R2 | Usuário logado, equipamento já disponível | Nenhuma alteração, retorna para home |
| R3 | Equipamento não existe (ID inválido) | Erro 404 |
| R4 | Usuário não autenticado | Redireciona para login |

### Casos de Teste Relacionados

| Regra | Caso de Teste |
|---|---|
| R1 | CT-08, CT-10 |
| R4 | CT-04 |
