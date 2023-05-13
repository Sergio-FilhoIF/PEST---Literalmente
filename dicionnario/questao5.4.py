# Crie um dicionário com o nome e a idade de três pessoas diferentes. Em seguida, use um loop para imprimir
# o nome e a idade de cada pessoa separadamente.
dicionario = {
    'sergio': 16,
    'mae':36
}

for nome, idade in dicionario.items():
    print(f"{nome} tem {idade}.")