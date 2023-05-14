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
    for nome, senha in usuarios.items():
        return print("Usuario não existi ❗.")
    if senha not in usuarios.values():
        return print('Senha incorreta ❌.')
    else:
        return print('Show!')
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
        apagar_usuario()

    elif op == 4:
        editar_usuario()

    elif op == 5:
        mostrar_usuario()

    elif op == 0:
        break