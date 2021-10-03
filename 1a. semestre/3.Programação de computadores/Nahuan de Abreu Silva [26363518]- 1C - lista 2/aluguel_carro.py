km_percorrido = float(input("Digite a quantidade de km percorrido com o carro: "))
dias = float(input("Digite a quantidade de dias que ficou com o carro: "))
soma_km = km_percorrido * 0.15
soma_dos_dias = dias * 60
total = soma_km + soma_dos_dias
print("O valor total a ser pago vai ser de R$", total)

