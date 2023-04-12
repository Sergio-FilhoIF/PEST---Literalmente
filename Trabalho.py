lista_de_conjuntos = []

def menu() :
    print()
    print("=-=" * 15)

    print(f"{'Menu': ^45}")
    print("""
    [1] - Criar Conjunto
    [2] - Adicionar Elemento
    [3] - Remover Elemento
    [4] - Mostrar Conjunto
    [0] - Sair
    """)
    print("=-=" * 15)

def criar_conjunto() :
    conjunto = []
    lista_de_conjuntos.append(conjunto)
    return lista_de_conjuntos

## verifica a função adicionar elemento
def add_elementos(indice, item):
    ## lista aux com o elemento inserido
    lista_de_conjuntos[indice-1].append(item)
    return lista_de_conjuntos

## verifica a função deletar elementos
def del_elementos(indice, item):
    flag = False
    ## verifica se o elemento está na lista
    if item in lista_de_conjuntos[indice-1]:
        ## remove o elemento da lista
        lista_de_conjuntos[indice-1].remove(item)
        flag = True
    ## verifica se o elemento existe ou não
    if not flag:
        print("O elemento não está na lista")
    return lista_de_conjuntos

## verifica a função mostrar conjunto
def mostrar_conjunto(indice):
    ## lista com os itens do conjunto
    print()
    print("A lista tem os elementos:")
    ## percorre a lista desejada
    for elemento in lista_de_conjuntos[indice-1]:
        print(elemento)


#menu principal
while True:
    menu()
    ## verifica a opção do usuario
    opcao = int(input("Digite o Número da opção: "))
    ## 
    while not opcao >= 0 and opcao <= 4:
        print("Digito invalido")
        opcao = int(input("Digite novamente:  "))
    if opcao == 1:
        print()
        criar_conjunto()
    if opcao == 2:
        print()
        indice = int(input("Digite o id do conjunto:  "))
        item = int(input("Digite um elemento a ser adicicionado:  "))
        add_elementos(indice, item)
    if opcao == 3:
        print()
        indice = int(input("Digite o id do conjunto que deseja alterar:   "))
        item = int(input("Digite o elemento que deseja apagar:  "))
        del_elementos(indice, item)
    if opcao == 4:
        print()
        indice = int(input("Digite o id do conjunto que deseja ser mostrado:   "))
        mostrar_conjunto(indice)
    if opcao == 0:
        break
