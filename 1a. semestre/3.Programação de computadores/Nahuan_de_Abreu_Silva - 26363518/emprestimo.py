casa = float(input("Digite o valor da casa que deseja comprar: "))
salario = float(input("Digite o valor do seu salário: "))
prazo = float(input("Em quantos anos pretende pagar a casa: "))

meses = prazo * 12
parcela = casa / meses

if prazo > (30 / 100) * salario:
    print("O seu empréstimo não foi aprovado.") 
else:
    print("O seu emprésitmo foi aproavado com sucesso.")