num1 = int(input("Digite um número: "))
num2 = []
total = 0
while(num1 != 0):
    num2.append(num1)
    num1 = int(input('Digite outro numero: '))
if(num1 == 0):
    for x in num2:
        total += x
    print('Soma dos numeros: ', total)
    print('Média aritmética: ', total / len(num2))
