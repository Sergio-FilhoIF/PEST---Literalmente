# Escreva um programa que crie um dicionário de produtos e seus preços. O programa deve permitir ao
# usuário adicionar novos produtos e preços, atualizar preços existentes e excluir produtos do dicionário. Cada
# produto deve estar relacionado a uma categoria. Considere as categorias: Bebida, Comida, Limpeza e
# Frutas.
produtos = {}
def menu():
    print('''
    [1] - Adicionar novo produtos ➕.
    [2] - Atualizar preços .
    [3] - Excluir produtos ❗.
    [0] - Sair ❌.
    ''')
    return int(input('Digite a opção: '))

def add_produto(nome_produto, categoria, preco_produto):
    produtos[nome_produto] = {'categoria': categoria,'preco': preco_produto}
    return print(produtos)

def atualizar_preco(nome_produto, categoria, preco_produto):
    produtos[nome_produto]['preco'] = preco_produto
    return print(produtos)

def del_produto(nome_produto):
    del produtos[nome_produto]
    return print(produtos)

while True:
    op = menu()
    if op == 1:
        nome_produto = input("Digite o nome do produto: ")
        categoria_produto = input("Digite a categoria do produto:")
        preco_produto = float(input("Digite o preço do produto: "))
        add_produto(nome_produto, categoria_produto, preco_produto)
    elif op == 2:
        nome_produto = input("Digite o nome do produto: ")
        categoria_produto = input("Digite a categoria do produto:")
        preco_produto = float(input(f"Digite o novo preço do produto({nome_produto}): "))
        atualizar_preco(nome_produto, categoria_produto, preco_produto)
    elif op == 3:
        nome_produto = input("Digite o nome do produto que deseja apagar: ")
        del_produto(nome_produto)
    elif op == 0:
        print('Tchau')
        break