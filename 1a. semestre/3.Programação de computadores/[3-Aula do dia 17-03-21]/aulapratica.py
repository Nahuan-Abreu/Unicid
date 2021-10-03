#import this -  filosofia do python

#---------exemplo 1---------------------------------------------------------------------------------

print("Meu nome eh Nahuan ")
print("Nahuan")

msg="Olá"
print(msg)

#----------------------- exemplo 2 ----------------------------------------------------------------------

print("Olá")  # "Pula" linha (padrão)

print("Boa noite", end = " ")  # Não "pula" linha

print("Tudo",end = "\t")  # Dá um espaço de tabulação

print("Bem?", end = "***")  # Não "pula linha e mostra ***

print("Espero que sim !", end = "FIM")  # Não "pula" linha e escreve FIM

#-------------------------- exemplo 3--------------------------------------------------------------------

a = 12 # variavel
b = 2  #variavel
print(a+b)

#-------------------- exemplo 4 -------------------------------------------------------------------------

salario = 1000
aumento = 5
novo_salario = salario + (salario * aumento / 100) # formula para o calculo do novo salario em 5% ou seja salario vezes 5 dividido por 100
print(novo_salario)

#------------------------------ exemplo 5 ---------------------------------------------------------------
a = 10
b = 20
print("A soma dos números é:", a + b)

#---------------------------------- exemplo 6 -----------------------------------------------------------

# se nao colocarmos o int que siginifica que oq o usuario vai escrever eh um numero inteiro
# se quiser mos colcor numeros com float, trocamos o int por float e conseguimos ver numeros com , ou pontos no caso

#a = float(input("Digite um número: "))
#a = float(input("Digite outro número: "))

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print(a + b)

#------------------------------ exemplo 7 ---------------------------------------------------------------

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print("O seu IMC é: ", round(imc, 2))

if (imc < 18.5) :
    print("Magreza")
elif(imc > 18.5 and imc < 24.9):
    print("Saudável")
elif(imc > 25 and imc < 29.9):
    print("Sobrepeso")
elif(imc >30 and imc < 34.9):
    print("Obesidade Grau 1")
elif(imc > 35 and imc < 39.9):
    print("Obesidade Grau 2 (severa)")

#----------------------- exemplo 8 ----------------------------------------------------------------------

"a" > "c"

ord("ç")

#------------------- exemplo 9 --------------------------------------------------------------------------

fizerSol = True
forFeriado = False
vouParaPraia = fizerSol and forFeriado
print(vouParaPraia)


fizerSol = True
forFeriado = True
vouParaPraia = fizerSol and forFeriado
print(vouParaPraia)

#------------------------ exemplo 10 --------------------------------------------------------------------

a = "python"

print(a[0], a[1], a[2],a[3], a[4], a[5])