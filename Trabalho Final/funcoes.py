# Funções que iram se repetir
    # Verificador de Erros
def verificador_dicionario(dicionario):
    if len(dicionario) == 0:
        print('===========================')
        print("Dicionario Vazio ❌.")
        print()
        print("Cadastre pelo menos um professor e um aluno")
        print('===========================')
        return False
    else:
        return True

    # Função de Salvar
def salvar():
    pass

# ------------------------------------------------------------------------
# Opções do menu das Turmas.
    # Opçao [1]
def criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores):
    verificador_professor = verificador_dicionario(dicionario_professores)
    verificador_aluno = verificador_dicionario(dicionario_alunos)
    lista_alunos = dicionario_alunos.get('Materia')
    if verificador_aluno == True and verificador_professor == True:
        for alunos in lista_alunos:
            print() 
        return True
    else:
        return False
    # Opçao [2]
def editar_turma():
    pass
    # Opçao [3]
def ver_turma():
    pass
    # Opçao [4]
def apagar_turma():
    pass

# ------------------------------------------------------------------------
# Opções do menu dos Professores.
    # Opçao [1]
def cadastrar_professor(nome_professor,dicionario_professor):
    
    
    # Opçao [2]
def editar_professor(nome_professor, dicionario_professores):
    if nome_professor in dicionario_professores:
        pass
    else:
        print('Esse professor não está cadastrado.')
    # Opçao [3]
def ver_dados_professor(dicionario):
    nome_professor = input("Digite o nome do professor que deseja vê os dados: ")
    matricula = 0
    for nome_professor in dicionario.keys():
        aux += 1
        print(f'{matricula} - {nome_professor}')
    # Opçao [4]
def apagar_professor():
    pass
    # Opçao [5]
def visualizar_turmas_professor():
    pass
    # Opçao [6]
def visualizar_alunos_turma_professor():
    pass

# ------------------------------------------------------------------------
# Opções do Menu dos Alunos.
    # Opçao [1]
def cadastrar_aluno(dicionario,lista_ids):
    print('===========================')
    nome_aluno = input("Digite o nome do aluno: ")

    lista_ids.append()
    dicionario[id] = nome_aluno
    print('===========================')

    # Opçao [2]
def editar_aluno():
    pass
    # Opçao [3]
def visualizar_aluno():
    pass
    # Opçao [4]
def apagar_aluno():
    pass



print('''
{{
'dados':{'nome': 'Cataryna, 'id':1}
}}
''')