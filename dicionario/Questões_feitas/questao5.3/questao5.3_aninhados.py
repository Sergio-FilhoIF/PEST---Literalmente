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

def add_produto(nome_produto, preco_produto, categoria):
    produtos[nome_produto] = nome_produto['categoria'][categoria], nome_produto['preco']=[preco_produto]
    return print(produtos)

add_produto('Coca cola', 4, 'bebida')