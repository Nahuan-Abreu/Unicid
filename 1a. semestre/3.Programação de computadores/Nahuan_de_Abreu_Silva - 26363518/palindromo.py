numero = str(input("Digite o número:"))
b = numero.split()
normal = " ".join(b)
aocontrario = ""
for letra in range(len(normal)-1, -1, -1):
    aocontrario += normal[letra]
print(normal, aocontrario)
if normal == aocontrario:
    print("O seu número é um palindromo")
else:
    print("O seu número não é um palidromo")
