# 📚 Sistema de Gerenciamento de Biblioteca (Console)

Este projeto é um sistema simples de gerenciamento de biblioteca desenvolvido em Python, utilizando o terminal e estruturas de dados básicas (listas e dicionários). Ideal para fins didáticos e projetos introdutórios.

---

## ✅ Funcionalidades

- **Cadastrar Autor**
  - Registra autores com `id`, `nome` e `data de nascimento`.
  - Evita duplicação de IDs.

- **Cadastrar Aluno**
  - Registra alunos com `id`, `nome`, `data de nascimento` e `email`.
  - Valida IDs únicos.

- **Adicionar Livro**
  - Permite cadastrar livros com `id`, `título`, `autor`, `data de cadastro` e `atualização`.
  - Só permite adicionar livros vinculados a autores já cadastrados.

- **Listar Autores e Livros**
  - Exibe todos os autores e livros com seus respectivos dados.
  - Livros mostram o ID do autor associado.

- **Pesquisar**
  - Permite buscar por nome de autor, título de livro ou nome de aluno.

- **Emprestar Livro**
  - Registra empréstimos entre alunos e livros.
  - Verifica disponibilidade do livro antes de emprestar.

- **Devolver Livro**
  - Atualiza o status do empréstimo e torna o livro novamente disponível.

- **Listar Empréstimos Ativos**
  - Mostra todos os livros que estão emprestados no momento, com nome do aluno, título do livro e data do empréstimo.

---

## 🛠 Estrutura de Dados

Os dados são armazenados em memória, nas seguintes listas:

- `autores`: dicionários com `id`, `nome` e `dataDeNascimento`
- `alunos`: dicionários com `id`, `nome`, `dataDeNascimento` e `email`
- `livros`: dicionários com `id`, `titulo`, `autor`, `autor_id`, `dataCadastro`, `dataAtualizacao` e `disponivel`
- `emprestimos`: dicionários com `aluno_id`, `livro_id`, `dataEmprestimo`, `dataDevolucao` e `devolvido`

---

## 🚀 Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git