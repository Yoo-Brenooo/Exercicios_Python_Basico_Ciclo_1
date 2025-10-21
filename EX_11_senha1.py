# Escreva um programa que pede que o usuário informe uma senha.
# O código deve comparar a senha informada pelo usuário com uma senha pré-definida no código armazenada em uma variável 
# Depois o código deve informar se a senha é correta ou incorreta.

# OUTPUT ESPERADO
# Exemplo 1:

# Digite a senha: 123123
# Senha incorreta

# Exemplo 2:

# Digite a senha: AC12
# Senha correta

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

senha_real = "1234"
senha = input("Digite uma senha: ")

if senha_real != senha:
    print("Senha incorreta!")
else:
    print("Senha correta")