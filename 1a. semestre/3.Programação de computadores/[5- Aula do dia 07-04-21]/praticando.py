# ----------exemplo 1---------------------------------------------------
a = int(input('Digite o valor A:'))
b = int(input('Digite o valor B:'))
c = int(input('Digite o Valor C:'))
delta = (b**2) - (4 * a * c)
print(f"{delta}")
if delta <=0:
  print("não exite raiz quandrada de numero negativo")
else:
  x1 = (-1*b + math.sqrt(delta)) / (2*a)
  x2 = (-1*b - math.sqrt(delta)) / (2*a)
  print(f'x1 vale: {x1} e x2 vale:{x2}')
# ----------exemplo 2---------------------------------------------------
def soma (x,y,z):
    return (x+y+z)
soma (1,2,3)
# vai retornar 6
# ----------exemplo 3---------------------------------------------------
def media(a,b):
    return((a+b)/2)
media (8.5)
vai retornar 6.5
# ----------exemplo 4---------------------------------------------------
# Fatorial de números digitados pelo usuário
def main():
  numeroDigitado = int(input("Digite um número inteiro e positivo:"))
  while numeroDigitado > 0:
    fat = calculaFatorial(numeroDigitado)
    print("O fatorial de",numeroDigitado,"é",fat)
    numeroDigitado = int(input("Digite um número inteiro e positivo:"))
def calculaFatorial(n):
  cont = 1
  fat = 1
  while cont <= n:
    fat = fat * cont
    cont = cont + 1
  return fat
main())
# ----------exemplo 5---------------------------------------------------
var_global = "Introdução ao Python"
def escreve_texto():
   var_global = "Planeta UNIX"
   var_local = "Engenharia de Software"
   print("Variável global:", var_global)
   print("Variável local:", var_local)
var_global = "Introdução ao Python"
escreve_texto()