from db import criar_tabela, cadastrar_usuario, login_usuario, consultar_usuarios


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(nome, email, senha)
            print("\nUsuário cadastrado com sucesso!")
        elif opcao == '2':
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            mensagem = login_usuario(email, senha)
            print(mensagem)
        elif opcao == '3':
            usuarios = consultar_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif opcao == '4':
            break
        else:
            print("\nOpção inválida!")


criar_tabela()
menu()
