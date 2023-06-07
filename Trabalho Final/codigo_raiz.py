# Importando todas as outras pastas.
from funcoes import *
from menus import *

# Dicionario das Turmas.
dicionario_turmas = {}
# Dicionario dos Professores.
dicionario_professores = {}
# Dicionario dos Alunos.
dicionario_alunos = {}

# Logica raiz do programa.
while True:
    op = menu_inicial()
    if op == '1':
        while True:
            op = menu_turmas()
            if op == '1':
                criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores)

            elif op == '2':
                editar_turma()
            elif op == '3':
                ver_turma()
            elif op == '4':
                apagar_aluno()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()

    elif op == '2':
        while True:
            op = menu_professores()
            if op == '1':
                nome_professor = input("Digite o nome do professor: ")
                cadastrar_professor(nome_professor)
            elif op == '2':
                id_professor = input("Digite o id do professor que voçê que editar: ")
                id_professor = int(id_professor)
                nome_professor_novo = input(f"Digite o novo nome do professor:'{dicionario_professores[id_professor]}': ")
                editar_professor(id_professor, nome_professor_novo, dicionario_professores)
            elif op == '3':
                ver_dados_professor()
            elif op == '4':
                apagar_professor()
            elif op == '5':
                visualizar_turmas_professor()
            elif op == '6':
                visualizar_alunos_turma_professor()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()

    elif op == '3':
        while True:
            op = menu_alunos()
            if op == '1':
                cadastrar_aluno()
            elif op == '2':
                editar_aluno
            elif op == '3':
                visualizar_aluno()
            elif op == '4':
                apagar_aluno()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()      

    elif op == 'sair':
        print("Programa Encerrado!😪")
        break
    else:
        print()
        print(f"Opção '{op}' invalida ❌.")
        print()

