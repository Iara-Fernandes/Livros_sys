# Exibição de mensagem de boas-vindas 
print("Bem-vindo ao sistema de gerenciamento de livros! Desenvolvido por Iara Fernandes")

# Lista de livros e variável de controle do ID
lista_livro = []  # Lista que armazenará os livros cadastrados
id_global = 0  

# Função para cadastrar livro
def cadastrar_livro(id):
    print("\nCadastro de Livro")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    
    # Criação de dicionário com os dados do livro
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    
    # Adiciona o livro à lista
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    while True:
        print("\nConsultar Livro")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nTodos os livros cadastrados:")
            for livro in lista_livro:
                print(livro)
        
        elif opcao == "2":
            try:
                id_consulta = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro["id"] == id_consulta:
                        print(livro)
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido.")
        
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_consulta.lower()]
            if encontrados:
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado para este autor.")
        
        elif opcao == "4":
            break
        
        else:
            print("Opção inválida")

# Função para remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro["id"] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("Id inválido.")
        except ValueError:
            print("Id inválido.")

# Programa principal (menu)
while True:
    print("\nMenu Principal")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        id_global += 1
        cadastrar_livro(id_global)

    elif escolha == "2":
        consultar_livro()

    elif escolha == "3":
        remover_livro()

    elif escolha == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")