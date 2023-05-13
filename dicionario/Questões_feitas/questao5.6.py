# Crie um dicionário com o nome e a pontuação de cinco jogadores diferentes. Em seguida, use um loop para
# calcular a média das pontuações e imprimir o resultado na tela
dicionario = {
    'paulo':10,
    'sergio':30,
    'rebeca':30,
    "ser":30,
    'palo':10
}
aux = 0
for ponto in dicionario.values():
    aux += ponto

print(aux/len(dicionario))