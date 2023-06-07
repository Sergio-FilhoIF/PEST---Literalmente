# # - O usuário deve contar um nome composto 'Vitoria Maria' e não pode conter números.✅
# # - Não pode ser cadastro alguém com o mesmo nome .✅
# # - A senha deve ter no mínimo 7 caracteres incluindo números e letras.✅
# # - O usuário só pode apagar ou editar caso esteja logado.
# # - Caso o usuário já esteja logado, ele não pode logar novamente. 
# # - Deve ter a opção de deslogar.
# aux = 0
# logado = False
# usuarios = {}
# def menu():
#     print('''
#     =-=-=-Sistema de Cadastros-=-=-=
#     # [1] - Cadastrar.
#     # [2] - Logar.
#     # [3] - Mostrar Usuarios.
#     # [0] - Sair.
#     -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#     ''')

# def menu_logado():
#     print('''
#     =-=-=-Sistema de Cadastros-=-=-=
#     # [1] - Cadastrar.
#     # [2] - Apagar.
#     # [3] - Editar.
#     # [4] - Mostrar Usuarios.
#     # [5] - deslogar.
#     # [0] - Sair.
#     -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#     ''')

# def cadastrar_usuario(nome,senha):
#     usuarios[nome] = senha
#     return print("Usuario cadastrado com sucesso ✅.")

# def logar(nome, senha):
#     if nome not in usuarios:
#         return print("Usuario não existi ❗.")
#     else:
#         if senha == usuarios[nome]:
#             print("Você está logado ✅.")
#             return True
#         else:
#             print("Login ou senha incorreta ❗.")

# def apagar_usuario(nome, senha, confirm_senha):
#     if senha == usuarios[nome] and confirm_senha == usuarios[nome]:
#         del usuarios[nome]
#         return print(f"Usuario '{nome}' apagado com sucesso ✅.")
#     else:
#         print("Login ou senha incorreta ❗.")

# def editar_usuario(nome, senha , confirm_senha):
#     if senha == usuarios[nome] and confirm_senha == usuarios[nome]:
#         novo_nome = input("Digite o novo nome de usuario: ")
#         if nome_usuario.replace(' ','').isalpha() == False:
#             print("A senha deve conter só letras.")
#         else:
#             aux = False
#             for nome in nome_usuario:
#                 if nome.isspace() == True:
#                     aux = True
                    
#             if aux == False:
#                 print("A o nome de usuario tem que ter nome composto.")
#             else:
#                 nova_senha = input("Digite a nova senha: ")
#                 if len(nova_senha) >= 7:
#                     if nova_senha.isalpha() == True:
#                         print("A senha tem que ter pelo menos um numero.")
#                     elif nova_senha.isdecimal() == True:
#                         print("A senha tem que ter pelo menos uma letra.")
#                     else:
#                         confirma_senha = input("Digite a confirmação da senha: ")
#                         if nova_senha == confirma_senha:
#                             usuarios[novo_nome] = usuarios.pop(nome)
#                             usuarios[novo_nome] = nova_senha
#                             for nomes in usuarios.keys():
#                                 print(nomes)
#                             return print("Usuario cadastrado com sucesso ✅.")
#                         else:
#                             return print("Confirmação da senha não é igual ❌.")
#     else:
#         return print("Confirmação de senha não é igual ❌.")

# def mostrar_usuario():
#     aux = 0
#     for nomes in usuarios.keys():
#         aux += 1
#         print(f'{aux} - {nomes}')


# while True:
#     if aux == 0:
#         if logado == False:
#             while True:
#                 menu()
#                 op = int(input("Escolha a opção: "))

#                 # Cadastrar
#                 if op == 1:
#                     nome_usuario = input("Digite seu nome: ")
                    
#                     if nome_usuario.replace(' ','').isalpha() == False:
#                         print("A senha deve conter só letras.")
#                         continue
#                     else:
#                         aux = False
#                         for nome in nome_usuario:
#                             if nome.isspace() == True:
#                                 aux = True
#                             else:
#                                 continue
#                         if aux == False:
#                             print("A o nome de usuario tem que ter nome composto.")
#                             continue
#                         else:
#                             if nome_usuario in usuarios:
#                                 print("Nome já existe.")
#                                 continue
#                             else:
#                                 senha_usuario = input("Digite sua senha: ")
#                                 if len(senha_usuario) >= 7:
#                                     if senha_usuario.isalpha() == True:
#                                         print("A senha tem que ter pelo menos um numero.")
#                                         continue
#                                     elif senha_usuario.isdecimal() == True:
#                                         print("A senha tem que ter pelo menos uma letra.")
#                                         continue
#                                     else:
#                                         cadastrar_usuario(nome_usuario, senha_usuario)
#                                 else:
#                                     print("A senha tem que ter mais de 6 Caracteris.")
                                    
#                 # Fazer login
#                 elif op == 2:
#                     nome_usuario = input("Digite o seu nome do usuario: ")
#                     if nome_usuario in usuarios:
#                         senha_usuario = input("Digite a senha do usuario: ")
#                         logado = logar(nome_usuario, senha_usuario)
#                         break
#                     else:
#                         print(f"{nome_usuario} Não está cadastrado.")
#                         continue

#                 # Mostrar usuario
#                 elif op == 5:
#                     mostrar_usuario()
#                 # Sair
#                 elif op == 0:
#                     aux += 1
#                     break

                
#         if logado == True:
#             while True:
#                 menu_logado()
#                 op = int(input("Escolha a opção: "))
#                 # Cadastrar
#                 if op == 1:
#                     nome_usuario = input("Digite seu nome: ")
#                     if nome_usuario.replace(' ','').isalpha() == False:
#                         print("A senha deve conter só letras.")
#                         continue
#                     else:
#                         aux = False
#                         for nome in nome_usuario:
#                             if nome.isspace() == True:
#                                 aux = True
#                             else:
#                                 continue
#                         if aux == False:
#                             print("A o nome de usuario tem que ter nome composto.")
#                             continue
#                         else:
#                             if nome_usuario in usuarios:
#                                 print("Nome já existe.")
#                                 continue
#                             else:
#                                 senha_usuario = input("Digite sua senha: ")
#                                 if len(senha_usuario) >= 7:
#                                     if senha_usuario.isalpha() == True:
#                                         print("A senha tem que ter pelo menos um numero.")
#                                         continue
#                                     elif senha_usuario.isdecimal() == True:
#                                         print("A senha tem que ter pelo menos uma letra.")
#                                         continue
#                                     else:
#                                         cadastrar_usuario(nome_usuario, senha_usuario)
#                                 else:
#                                     print("A senha tem que ter mais de 6 Caracteris.")
                
#                 # Fazer login
#                 elif op == 2:
#                     nome_usuario = input("Digite o Usuario que deseja deletar: ")

#                     if nome_usuario in usuarios:
#                         senha_usuario = input("Digite a senha: ")
#                         confirm_senha = input("Digite a confirmação de senha: ")
#                         apagar_usuario(nome_usuario,senha_usuario,confirm_senha)
#                     else:
#                         print("Usuario não existe.")
#                         continue

#                 # Editar Usuario
#                 elif op == 3:
#                     for nomes in usuarios.keys():
#                         print(nomes)
#                     nome_usuario = input("Digite o nome do usuario que deseja editar: ")
#                     if nome_usuario in usuarios:
#                         senha_usuario = input("Digite a senha: ")
#                         confirm_senha = input("Digite a senha de confirmação: ")
#                         editar_usuario(nome_usuario, senha_usuario, confirm_senha)
#                     else:
#                         print("Usuario não existe.")

#                 # Mostrar usuario
#                 elif op == 4:
#                     mostrar_usuario()

#                 elif op == 5:
#                     print("Tchau!")
#                     logado = False
#                 # Sair
#                 elif op == 0:
#                     break
#     else:
#         break
dic = {
    1:'sergio',
    2:'caty'
}
for matricula in dic.keys():
    matricula +=1

print(matricula)