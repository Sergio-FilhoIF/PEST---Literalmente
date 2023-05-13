# Crie um dicionário com o nome e a idade de três pessoas diferentes. Em seguida, calcule a média de idade
# dessas pessoas.
dicionario = {
    'sergio': 16,
    'mae':36
}
aux = 0
for nome, idade in dicionario.items():
    print(f"{nome} tem {idade}.")
    aux += idade

print((aux/len(dicionario)))