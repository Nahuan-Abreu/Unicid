#----------------exemplo 1------------------------------
primos = [2, 3, 5, 7, 11]
indice = 0
while(indice < len (primos)):
    print("elementos de indice %d = %d"%(indice, primos[indice]))
    indice +=1
#----------------exemplo 2 -----------------------------
for letras in 'Python':
    print(letras, end='\t')
#------------------exemplo 3----------------------------
frutas = ['banana', 'maca', 'manga']
for fruta in frutas:
    print(fruta)
#----------------------exemplo 4------------------------
nome = []
for i in range(3):
    var_nome = input("Digite seu nome:")
    nome.append(var_nome)
#-------------------exemplo 5 ---------------------------
i = 2 
while True:
    if i % 3 == 0:
        break
    print(i)
    i +=2
#--------------------exemplo 6---------------------------
for num in range(2,10):
    if (num % 2 == 0):
        print("Achou um número par:",num, end = '  ')
        continue
    print("Procurando...")
#-----------------exemplo 7 -----------------------------
impostos = ['MEI', 'Simples']
for impostos in impostos:
    if impostos.startswith("S"):
        continue
    print (impostos)
#----------------exemplo 8-------------------------------
lista = ['banana', 'maca', 'ameixa']
for i in lista:
    print(i)
#---------------exemplo 9--------------------------------
#for i (contador/iterador) in impostos (é a lista)

