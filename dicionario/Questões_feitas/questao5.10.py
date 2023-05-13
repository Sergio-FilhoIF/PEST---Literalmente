# Escreva um programa que conte o número de ocorrências de cada letra em uma frase. O programa deve ler
# uma frase do usuário, separar suas letras, armazená-las em um dicionário e imprimir o número de
# ocorrências para cada letra.

frase = 'Parabens pra voce'
frase = frase.replace(' ', '').lower()
dicionario = {}
isso = {}
for letra in frase:
    if letra in dicionario:
        dicionario[letra] = dicionario[letra] + 1
    else:
        dicionario[letra] = 1
# OU
for letras in frase:
    isso[letras] = isso.get(letras,0) + 1

print(isso)
print(dicionario)