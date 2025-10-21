# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: "))
porcentagem = float(input("Digite o valor do desconto: "))
desconto = preco * (porcentagem / 100) 
produto = preco - desconto

print(f"Produto: {nome}")
print(f"Preço: {preco}")
print(f"Porgentagem: {porcentagem}%")
print(f"O {nome} com {desconto}% de desconto custará R${preco} ")