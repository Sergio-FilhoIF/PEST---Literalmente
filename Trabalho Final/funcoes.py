dicio
# Funções que iram se repetir
    # Verificador de Erros
def verificador_dicionario(dicionario_professor, diocionario_aluno):
    if len(dicionario_professor) == 0 and len(diocionario_aluno == 0):
        print("Dicionario Vazio ❌.")
        print()
        print("Cadastre pelo menos um professor e um aluno")
        return False
    else:
        return True

    # Função de Salvar
def salvar():
    pass

# ------------------------------------------------------------------------
# Opções do menu das Turmas.
    # Opçao [1]
def criar_turma(dicionario):
    print('='*20)
    verificador = verificador_dicionario(dicionario)
    if verificador == True:
        print("oi")
        
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
def cadastrar_professor():
    pass
    # Opçao [2]
def editar_professor():
    pass
    # Opçao [3]
def ver_dados_professor():
    pass
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
def cadastrar_aluno():
    pass
    # Opçao [2]
def editar_aluno():
    pass
    # Opçao [3]
def visualizar_aluno():
    pass
    # Opçao [4]
def apagar_aluno():
    pass