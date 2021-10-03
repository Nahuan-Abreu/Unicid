tabuada = int(input('Digite o numero da tabuada: '))
comeco = int(input('Digite o inicio da tabuada: '))
final = int(input('Digite o fim da tabuada: '))

for x in range(comeco, final + 1):
    print(f"{tabuada} x {x} = {tabuada * x}")