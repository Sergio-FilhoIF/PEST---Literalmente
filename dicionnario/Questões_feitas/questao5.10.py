# Escreva um programa que conte o número de ocorrências de cada letra em uma frase. O programa deve ler
# uma frase do usuário, separar suas letras, armazená-las em um dicionário e imprimir o número de
# ocorrências para cada letra.

frase = 'Parabens pra voce'
frase = frase.replace(' ', '').lower()
dicionario = {}
for i in range(len(frase)):
    if frase[i] in dicionario:
        dicionario[frase[i]] = dicionario[frase[i]] + 1
    else:
        dicionario[frase[i]] = 1
print(dicionario)