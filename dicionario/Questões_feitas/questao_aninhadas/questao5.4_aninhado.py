# Escreva um programa que crie um dicionário de nomes de alunos e suas notas em disciplinas. Cada aluno
# deve estar associado a duas disciplinas (Português e Matemática) e cada disciplina deve ter uma ou mais
# notas. O programa deve permitir ao usuário adicionar novos alunos e notas, atualizar notas existentes e
# excluir alunos do dicionário. O programa também deve calcular a média de notas do aluno por disciplina.
boletin = {}
def menu():
    print('''
    [1] - Adicionar Aluno com nota(s). ➕.
    [2] - Atualizar notas.
    [3] - Excluir Aluno ❗.
    [4] - Calcular media.
    [0] - Sair ❌.
    ''')
    return int(input('Digite a opção: '))

def add_aluno_nota(nome_aluno, lista_nota_aluno_matematica, lista_nota_aluno_portugues):
    boletin[nome_aluno] = {'matematica': lista_nota_aluno_matematica,'portugues': lista_nota_aluno_portugues}
    print('=-'*7)
    print(boletin)
    print()
    print('alunos matriculado.')
    print('=-'*7)
    

def atualizar_notas(nome_aluno, lista_nota_aluno_matematica, lista_nota_aluno_portugues):
    boletin[nome_aluno]['matematica'] = lista_nota_aluno_matematica
    boletin[nome_aluno]['portugues'] = lista_nota_aluno_portugues
    print('=-'*7)
    print(boletin)
    print()
    print('Notas atualizadas.')
    print('=-'*7)

def excluir_aluno(nome_aluno):
    del boletin[nome_aluno]
    print('=-'*7)
    print(boletin)
    print()
    print('aluno deletado.')
    print('=-'*7)

def calc_media(nome_aluno):
    media = sum(boletin[nome_aluno]['matematica'])/len(boletin[nome_aluno]['matematica'])
    print('=-'*7)
    print(boletin['matematica'])
    print()
    print(f'Sua media em matematica é: {media}.')
    print('=-'*7)

    media = sum(boletin[nome_aluno]['portugues'])/len(boletin[nome_aluno]['portugues'])
    print('=-'*7)
    print(boletin['portugues'])
    print()
    print(f'Sua media em portugues é: {media}.')
    print('=-'*7)

while True:
    op = menu()
    if op == 1:
        lista_notas_matematica = []
        lista_notas_portugues = []
        nome_aluno = input("Digite o nome do aluno: ")
        while True:
            nota_aluno = float(input("Digite a nota de matematica: "))
            lista_notas_matematica.append(nota_aluno)
            pergunta = input('Digite S/N: ')
            if pergunta not in 'nN':
                continue
            else:
                break
        
        while True:
            nota_aluno = float(input("Digite a nota de portugues: "))
            lista_notas_portugues.append(nota_aluno)
            pergunta = input('Digite S/N: ')
            if pergunta not in 'nN':
                continue
            else:
                break
        add_aluno_nota(nome_aluno, lista_notas_matematica, lista_notas_portugues)

    elif op == 2:
        lista_notas_matematica = []
        lista_notas_portugues = []
        nome_aluno = input("Digite o nome do aluno: ")
        while True:
            nota_aluno = float(input("Digite a nova nota de matematica: "))
            lista_notas_matematica.append(nota_aluno)
            pergunta = input('Digite S/N: ')
            if pergunta not in 'nN':
                continue
            else:
                break
        
        while True:
            nota_aluno = float(input("Digite a nova nota de portugues: "))
            lista_notas_portugues.append(nota_aluno)
            pergunta = input('Digite S/N: ')
            if pergunta not in 'nN':
                continue
            else:
                break
        add_aluno_nota(nome_aluno, lista_notas_matematica, lista_notas_portugues)
    
    elif op == 3:
        nome_aluno = input("Digite o nome do aluno que queira excluir: ")
        excluir_aluno(nome_aluno)
    
    elif op == 4:
        nome_aluno = input('Digite o nome do aluno que queira calcular a sua media final: ')
        calc_media(nome_aluno)

    elif op == 0:
        break