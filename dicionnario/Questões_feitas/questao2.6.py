# Altere o exercício anterior para adicionar as funções de adicionar um item (par chave-valor), remover um item
# e limpar o dicionário.

dicionario = {}

def menu():
    print('''
    [1] - Adicionar um item
    [2] - Remover um item
    [3] - Limpar o Dicionario
    [0] - Sair do programa
    ''')

def add_item(chave, valor):
    dicionario[chave] = valor
    print(dicionario)
    return print("Item adicionado com sucesso ✅")

def remover_item(chave):
    if chave not in dicionario:
        print(f"Não existe um item com {chave} ❌.")
    else:
        del dicionario[chave]
        print(dicionario)
        return print("Item removido com sucesso ✅.")

def limpar_tudo():
    dicionario.clear()
    print(dicionario)
    return print("Dicionario limpado com sucesso ✅.")

while True:
    menu()
    op = int(input("Digite a opção: "))

    if op == 1:
        chave = input("Digite o nome da chave: ")
        valor = input(f"Digite o valor da chave {chave}: ")
        add_item(chave, valor)
    elif op == 2:
        chave = input("Digite o nome do item que queira remover: ")
        remover_item(chave)
    elif op == 3:
        limpar_tudo()
    elif op == 0:
        print("Programa fechado ✅.")
        break