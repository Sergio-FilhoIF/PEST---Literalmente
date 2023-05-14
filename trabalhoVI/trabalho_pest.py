usuarios = {}
def menu():
    print('''
    =-=-=-Sistema de Cadastros-=-=-=
    [1] - Cadastrar.
    [2] - Logar.
    [3] - Apagar.
    [4] - Editar.
    [5] - Mostrar Usuarios.
    [0] - Sair.
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    ''')
    return

def cadastrar_usuario(nome,senha):
    usuarios[nome] = senha
    return print("Usuario cadastrado com sucesso ✅.")

def logar(nome, senha):
    if nome not in usuarios:
        return print("Usuario não existi ❗.")
    else:
        if senha == usuarios[nome]:
            return print("Você está logado ✅.")
        else:
            print("Login ou senha incorreta ❗.")

def apagar_usuario(nome, senha, confirm_senha):
    if nome not in usuarios:
        print("Usuario não existe ❗.")
    else:
        if senha == usuarios[nome] and confirm_senha == usuarios[nome]:
            del usuarios[nome]
            return print(f"Usuario '{nome}' apagado com sucesso ✅.")
        else:
            print("Login ou senha incorreta ❗.")

def editar_usuario(nome, senha , confirm_senha):
    if nome not in usuarios:
        print("Usuario não existe ❗.")
    else:
        if senha == usuarios[nome] and confirm_senha == usuarios[nome]:
            novo_nome = input("Digite o novo nome de usuario: ")
            nova_senha = input("Digite a nova senha: ")
            confirma_senha = input("Digite a confirmação da senha: ")
            if nova_senha == confirma_senha:
                usuarios[novo_nome] = usuarios.pop(nome)
                usuarios[novo_nome] = nova_senha
                for nomes in usuarios.keys():
                    print(nomes)
                return print("Usuario cadastrado com sucesso ✅.")
            else:
                return print("Confirmação da senha não é igual ❌.")
        else:
            return print("Confirmação de senha não é igual ❌.")

def mostrar_usuario():
    aux = 0
    for nomes in usuarios.keys():
        aux += 1
        print(f'{aux} - {nomes}')

while True:
    menu()
    op = int(input("Escolha a opção: "))
    if op == 1:
        nome_usuario = input("Digite seu nome: ")
        senha_usuario = input("Digite sua senha: ")
        cadastrar_usuario(nome_usuario, senha_usuario)

    elif op == 2:
        nome_usuario = input("Digite o seu nome do usuario: ")
        senha_usuario = input("Digite a senha do usuario: ")
        logar(nome_usuario, senha_usuario)

    elif op == 3:
        nome_usuario = input("Digite o nome do usuario que queira deletar: ")
        senha_usuario = input("Digite a senha: ")
        confirm_senha = input("Digite a confirmação da senha: ")
        apagar_usuario(nome_usuario, senha_usuario, confirm_senha)

    elif op == 4:
        for nomes in usuarios.keys():
            print(nomes)
        nome_usuario = input("Digite o nome do usuario: ")
        senha_usuario = input("Digite a senha: ")
        confirm_senha = input("Digite a senha de confirmação: ")
        editar_usuario(nome_usuario, senha_usuario, confirm_senha)

    elif op == 5:
        mostrar_usuario()

    elif op == 0:
        break