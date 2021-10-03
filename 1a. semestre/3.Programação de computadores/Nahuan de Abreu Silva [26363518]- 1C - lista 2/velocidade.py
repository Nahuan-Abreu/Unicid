velocidade_do_caro = float(input("Digite a velocidade do carro: "))
velocidade_acima = velocidade_do_caro - 80
if velocidade_do_caro <= 80:
    print("Tudo certo!")
else:
    print("Você vai ser mutado!")
    total = velocidade_acima * 5
    print(f"Sua multa será em R${total} pois passou {velocidade_acima} km/h do limite")
