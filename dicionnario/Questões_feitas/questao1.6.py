#Escreva um programa que crie um dicionário com 10 palavras e suas definições. O programa deve solicitar
#ao usuário cada chave e cada valor. Após adicionar as 10 palavras o usuário poderá pesquisar uma palavra e
#exibir sua definição correspondente.

dicionario = {}
for i in range(2):
    chave = input("Digite o nome da chave: ")
    valor = input(f"Digite o valor da chave {chave} : ")
    dicionario[chave] = valor
print(dicionario)