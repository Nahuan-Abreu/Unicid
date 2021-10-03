numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação: (1-Adição), (2-Subtração), (3-Divisão) ou (4-Multiplicação): "))
if operacao == 1:
    soma= numero1 + numero2
    print(f"O resultado da soma é: {soma}") 
elif operacao == 2:
    sub = numero1 - numero2
    print(f"O resultado da subtração é: {sub}")
elif operacao == 3:
    div = numero1 / numero2
    print(f"O resultado da divisão é: {div}")
elif operacao == 4:
    mult = numero1 * numero2
    print(f"O resultado da divisão é: {mult}")
else:
    print("Esolha umas das opicões acimda 1 à 4 !!")