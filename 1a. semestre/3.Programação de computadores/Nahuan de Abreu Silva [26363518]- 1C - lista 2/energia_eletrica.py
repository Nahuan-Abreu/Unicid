consumo = float(input("Digite o valor de consumo em kWh: "))
tipo = str(input("Coloque o tipo instalação: (R - Residencial) - (C - Comercial) - (I - Industrial) "))
if tipo == "R" or tipo == "r":
    if consumo <= 500:
        conta = consumo * 0.40
        print(f"Valor da conta a ser paga R$ {conta}")
    else:
        conta = consumo * 0.65
        print(f"Valor da conta a ser paga R$ {conta}")
elif tipo == "C" or tipo == "c":
    if consumo <= 1000 :
        conta = consumo * 0.55
        print(f"Valor da conta a ser paga R$ {conta}")
    else:
        conta = consumo * 0.60
        print(f"Valor da conta a ser paga R$ {conta}")
elif tipo == "I" or tipo == "i":
    if consumo <= 5000 :
        conta = consumo * 0.55
        print(f"Valor da conta a ser paga R$ {conta}")
    else:
        conta = consumo * 0.60
        print(f"Valor da conta a ser paga R$ {conta}")
else:
    print ("Selecione umas opções de instalação: (R - Residencial) - (C - Comercial) - (I - Industrial)")
