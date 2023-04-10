'''def menu():
    print("""
    [1] - Criar Conjuto
    [2] - Adicionar Elemento
    [3] - Remover Elemento
    [4] - Mostrar Elementos
    [0] - Sair do Programa
    """)
def criar_elemento():
    print("""

    """)'''
conjuntos = {}

def menu():
    opcoes = ['1 - Criar conjunto', '2 - Adicionar elemento', '3 - Remover elemento', '4 - Mostrar conjuntos', '0 - Sair']
    for opcao in opcoes:
        print(opcao)
    escolha = int(input('Escolha uma opção: '))

def criar_conjunto():
    id = len(conjuntos) + 1
    conjuntos[id] = set()
    print(f'Conjunto {id} criado.')
    return conjuntos[id]

def add_elemento(id, elemento):
    if id in conjuntos:
        conjuntos[id].add(elemento)
        print(f'Elemento {elemento} adicionado ao conjunto {id}.')
    else:
        print(f'Conjunto {id} não existe.')

def del_elemento(id, elemento):
    if id in conjuntos:
        if elemento in conjuntos[id]:
            conjuntos[id].remove(elemento)
            print(f'Elemento {elemento} removido do conjunto {id}.')
        else:
            print(f'O elemento {elemento} não pertence ao conjunto {id}.')
    else:
        print(f'Conjunto {id} não existe.')

def mostrar_conjunto(id):
    if id in conjuntos:
        print(f'Conjunto {id}: {conjuntos[id]}')
    else:
        print(f'Conjunto {id} não existe.')

while True:
    escolha = menu()
    if escolha == 0:
        print('Encerrando o programa.')
        break
    elif escolha == 1:
        criar_conjunto()
    elif escolha == 2:
        id = int(input('Informe o id do conjunto: '))
        elemento = input('Informe o elemento que deseja adicionar: ')
        add_elemento(id, elemento)
    elif escolha == 3:
        id = int(input('Informe o id do conjunto: '))
        elemento = input('Informe o elemento que deseja remover: ')
        del_elemento(id, elemento)
    elif escolha == 4:
        id = int(input('Informe o id do conjunto: '))
        mostrar_conjunto(id)
    else:
        print('Opção inválida. Tente novamente.')
