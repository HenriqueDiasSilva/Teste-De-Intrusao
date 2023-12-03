from db import criar_tabela, cadastrar_usuario, login_usuario


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")

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
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    criar_tabela()
    menu()
