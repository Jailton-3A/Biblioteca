autores = []
livros = []
alunos = []
emprestimos = []

def cadastroAutor():
    autor = {
        "id": int(input("Digite o id do autor ")),
        "nome": input("Digite o nome do autor "),
        "dataDeNascimento" : input("Digite a data de nascimento do autor ")
    }
    while any(au["id"] == autor["id"] for au in autores):
        autor["id"] = int(input("ID já utilizado! Digite outro ID "))
    autores.append(autor)

def cadastroAlunos():
    aluno = {
        "id": int(input("Digite o id do aluno ")),
        "nome": input("Digite o nome do aluno "),
        "dataDeNascimento" : input("Digite a data de nascimento do aluno "),
        "email" : input("Digite o email do aluno ")
    }
    while any(a["id"] == aluno["id"] for a in alunos):
        aluno["id"] = int(input("ID já utilizado! Digite outro ID "))
    alunos.append(aluno)

def adicionarLivro():
    livro = {
        "id": int(input("Digite o identificador único do livro: ")),
        "titulo": input("Digite o título do livro: "),
        "autor": input("Digite o nome do autor: "),
        "disponivel": True,
        "dataCadastro": input("Digite a data que o livro foi cadastrado: "),
        "dataAtualizacao": input("Digite a data de atualização do livro: ")
    }

    while any(l["id"] == livro["id"] for l in livros):
        livro["id"] = int(input("ID já utilizado! Digite outro ID: "))

    autores_encontrados = [a for a in autores if a["nome"].lower() == livro["autor"].lower()]

    if len(autores_encontrados) == 0:
        print(" Autor não encontrado! Cadastre o autor primeiro.\n")
        return
    elif len(autores_encontrados) > 1:
        print(" Há mais de um autor com esse nome! Selecione pelo ID:")
        for a in autores_encontrados:
            print(f"ID: {a['id']} - Nome: {a['nome']} - Nascimento: {a['dataDeNascimento']}")

        autor_id = int(input("Digite o ID do autor correto: "))
        
        while not any(a["id"] == autor_id for a in autores_encontrados):
            autor_id = int(input("ID inválido! Digite um ID válido da lista: "))

        livro["autor_id"] = autor_id
        print(f" Autor com ID {autor_id} selecionado com sucesso!")

    else:
        livro["autor_id"] = autores_encontrados[0]["id"]
        print(f" Autor {livro['autor']} encontrado!")

    livros.append(livro)
    print(f" Livro '{livro['titulo']}' cadastrado com sucesso!\n")

def emprestarLivro():
    aluno_id = int(input("Digite o ID do aluno que está pegando o livro emprestado: "))
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if not aluno:
        print("Aluno não encontrado!")
        return

    livro_id = int(input("Digite o ID do livro que será emprestado: "))
    livro = next((l for l in livros if l["id"] == livro_id), None)
    if not livro:
        print("Livro não encontrado!")
        return

    if not livro["disponivel"]:
        print("Livro já está emprestado!")
        return

    emprestimo = {
        "aluno_id": aluno_id,
        "livro_id": livro_id,
        "dataEmprestimo": input("Digite a data do empréstimo: "),
        "dataDevolucao": None,
        "devolvido": False
    }
    emprestimos.append(emprestimo)
    livro["disponivel"] = False
    print(f"Livro '{livro['titulo']}' emprestado para {aluno['nome']}.")

def devolverLivro():
    livro_id = int(input("Digite o ID do livro a ser devolvido: "))
    emprestimo = next((e for e in emprestimos if e["livro_id"] == livro_id and not e["devolvido"]), None)
    
    if not emprestimo:
        print("Nenhum empréstimo ativo encontrado para este livro.")
        return

    emprestimo["dataDevolucao"] = input("Digite a data da devolução: ")
    emprestimo["devolvido"] = True

    for livro in livros:
        if livro["id"] == livro_id:
            livro["disponivel"] = True
            break

    print("Livro devolvido com sucesso!")

def listarEmprestimosAtivos():
    print("\n--- Empréstimos Ativos ---")
    ativos = [e for e in emprestimos if not e["devolvido"]]

    if not ativos:
        print("Nenhum empréstimo ativo no momento.")
        return

    for e in ativos:
        aluno = next((a for a in alunos if a["id"] == e["aluno_id"]), {"nome": "Desconhecido"})
        livro = next((l for l in livros if l["id"] == e["livro_id"]), {"titulo": "Desconhecido"})
        
        print(f"Aluno: {aluno['nome']} | Livro: {livro['titulo']} | Data do Empréstimo: {e['dataEmprestimo']}")

while True:
    print("\n1 - Cadastrar Autor")
    print("2 - Adicionar Livro")
    print("3 - Cadastrar Aluno")
    print("4 - Lista de Autores")
    print("5 - Listar Livros")
    print("6 - Emprestar Livro")
    print("7 - Devolver Livro")
    print("8 - Listar Empréstimos Ativos")
    print("9 - Pesquisa")
    print("0 - Sair")
    opcao = int(input("Digite uma opção: "))

    if opcao == 0:
        print("Saindo...")
        break
    elif opcao == 1:
        cadastroAutor()
    elif opcao == 2:
        adicionarLivro()
    elif opcao == 3:
        cadastroAlunos()
    elif opcao == 4:
        print("\n Lista de Autores:")
        for a in autores:
            print(f"ID: {a['id']} - Nome: {a['nome']} - Nascimento: {a['dataDeNascimento']}")
        print()
    elif opcao == 5:
        print("\n Lista de Livros:")
        for l in livros:
            print(f"ID: {l['id']} - Título: {l['titulo']} - Autor ID: {l['autor_id']}")
        print()
    elif opcao == 6:
        emprestarLivro()
    elif opcao == 7:
        devolverLivro()
    elif opcao == 8:
        listarEmprestimosAtivos()
    elif opcao == 9:
        while True:
            print("1 - Pesquisar Autor")
            print("2 - Pesquisar Livro")
            print("3 - Pesquisar Aluno")
            pesquisa = int(input("Digite uma das opções de pesquisa: "))
            opcao == "-1"
            break
        if pesquisa == 1:
            nomeLivro = input("Digite o nome do autor que deseja encontrar: ")
            for a in autores:
                if nomeLivro == a["nome"]:      
                    print(f"ID : {a['id']} - Nome : {a['nome']} - Data de Nascimento : {a['dataDeNascimento']}")
                else:
                    print("Autor não encontrado")
        elif pesquisa == 2:
            tituloLivro = input("Digite o titulo do livro que deseja encontrar: ")
            for l in livros:
                if nomeLivro == l["titulo"]:
                    print(f"ID : {l['id']} - Titulo : {l['titulo']} - Autor : {l['autor']} - Disponivel? : {l['disponivel']} - Data de Cadastro {l['dataCadastro']} - Data de Atualização - {l['dataAtualizacao']}")
                else:
                    print("Livro não encontrado")

        elif pesquisa == 3:
            nomeAluno = input("Digite o nome do aluno que deseja encontrar: ")
            for al in autores:
                if nomeAluno == al["nome"]:
                    print(f"ID : {al['id']} - Nome : {al['nome']} - Data de Nascimento : {al['dataNascimento']} - Email : {al['email']}")
                else:
                    print("Aluno não encontrado")
            
    else:
        print("Opção inválida! Tente novamente.")