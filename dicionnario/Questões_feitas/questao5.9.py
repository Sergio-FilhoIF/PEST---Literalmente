# Escreva um programa que conte o número de ocorrências de cada palavra em uma frase. O programa deve
# ler uma frase do usuário, separar as palavras, armazená-las em um dicionário e imprimir o número de
# ocorrências para cada palavra.

frase = 'Um elefante incomoda muita gente, dois elefantes incomodam, incomodam muito mais'
frase = frase.lower().replace(',', '').split()
dicionario = {}

for palavra in frase:
    if palavra in dicionario:
        dicionario[palavra] = dicionario[palavra] + 1
    else:
        dicionario[palavra] = 1
print(dicionario)