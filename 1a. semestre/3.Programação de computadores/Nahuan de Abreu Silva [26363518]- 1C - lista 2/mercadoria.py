preco = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
porcentagem_do_desconto = preco * desconto / 100
pagar = preco - porcentagem_do_desconto
print("Um desconto de", desconto, "em uma mercadoria de R$ ", preco)
print("vale R$", porcentagem_do_desconto)
print("O valor a pagar é de R$",  pagar)