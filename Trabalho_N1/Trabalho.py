# Plataforma de estudo de conjuntos
# O seu projeto consiste em iniciar a criação de uma plataforma de estudo de conjuntos matemáticos para alunos. A plataforma deve permitir que o aluno crie conjuntos e realize operações com eles.

# **Requisitos e funcionalidades:**
# -  O usuário pode criar quantos conjuntos quiser. Cada conjunto terá um $id$ (identificador único iniciado em "1").
# - O programa deve possuir uma interface ("menu"), pelo qual o usuário vai escolher o que fazer (criar conjunto, adicionar elemento, remover elemento e mostrar conjuntos).
# - Deve possuir as seguintes funções (mas não se limite a apenas elas):
#     - ```menu()``` essa função deve criar um menu e \underline{retornar} a opção que o usuário escolher no menu.
#     - ```criar_conjunto()``` essa função deve criar e \underline{retornar} um conjunto vazio (sem elementos).
#     - ```add_elemento(id, elemento)``` o usuário informará o conjunto, através do id, e qual elemento quer adicionar. Será adicionado apenas um por vez. 
#     - ```del_elemento(id, elemento)``` o usuário informará o conjunto, através do id, e qual elemento quer deletar. Será apagado apenas um por vez. 
#     - ```mostrar_conjunto(id)``` essa função mostrará os elementos de um conjunto específico (a partir do seu id).
# **NOTA**: Este projeto pode ser feito em equipe de até 4 pessoas e enviado pelo SUAP. Cada membro da equipe deve contribuir com a implementação do programa e com a documentação do projeto. Só serão aceitos os conceitos vistos em sala de aula (if, else, while, for, listas e funções). A nota será composta por:
# - 1 ponto por cada função (solicitada acima) criada corretamente (total: 5 pontos).
# - 1 ponto pela lógica utilizada.
# - 1 ponto pelas proteções implementadas.
# - 1 ponto pela organização, documentação e nomenclatura das variáveis e funções.
# - 2 pontos pelos recursos utilizados no código (estritamente o que foi visto até função).




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
