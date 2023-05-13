# Crie um programa que armazene a quantidade de letras em cada palavra de uma lista de palavras. A lista
# deve conter as palavras "casa", "carro" e "bicicleta". O programa deve imprimir um dicionário contendo cada
# palavra como chave e a quantidade de letras como valor.
lista = ["casa", "carro", "bicicleta"]
dicionario = {}
for palavra in lista:
    dicionario[palavra] = len(palavra)
print(dicionario)