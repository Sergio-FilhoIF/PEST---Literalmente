# Suponha que você esteja trabalhando com um sistema de votação e precisa contar a quantidade de votos de
# cada candidato. Você tem uma lista com os números correspondentes aos candidatos votados. Crie um
# programa que calcule a quantidade de votos para cada candidato e armazene essa informação em um
# dicionário. Ao final, imprima o dicionário contendo cada candidato como chave e a quantidade de votos como
# valor.
lista = [1, 2, 3, 1, 2, 1, 3, 3, 1, 2]
dicionario = {}
for votos in lista:
    dicionario[votos] = lista.count(votos)
print(dicionario)