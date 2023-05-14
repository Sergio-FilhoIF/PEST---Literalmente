# Crie um dicionário em Python para ler e armazenar as notas de um aluno em uma disciplina. O dicionário
# deve ter como chaves os nomes das disciplinas (por exemplo, "matemática", "português", "história") e como
# valores as notas do aluno nessas disciplinas.
diciplinas = {}
while True:
    materia = input("Digite a materia: ")
    nota = float(input("Digite a nota de {materia}: "))
    op = input("Deseja Sair digite s/n: ")
    for materias,notas in diciplinas:
        print(f"Na materia: {materia} a nota é: {nota}")
    if op not in 'sS':
        diciplinas[materia] = nota
        print(diciplinas)
    else:
        break