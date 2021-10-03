while True:
  valor = float(input("Digite o valor a pagar:"))
  if valor == 0:
    print("Foi digitado o valor R$0,00.")
    break
  if valor < 0.01:
    print("Valor inválido!")
    break
  cédulas = 0
  atual = 100
  apagar = valor
  while True:
    if atual <= apagar:
      apagar -= atual
      cédulas += 1
    else:
      if atual >= 1:
        print(f"{cédulas} cédula(s) de R${atual}")
      else:
        print(f"{cédulas} moeda(s) de R${atual:5.2f}")
      if apagar < 0.01:
        break
      elif atual > 100:
        atual == 100
      elif atual == 100:
        atual = 50
      elif atual == 50:
        atual = 20
      elif atual == 20:
        atual = 10
      elif atual == 10:
        atual = 4
      elif atual == 4:
        atual = 1
      elif atual == 1:
        atual = 0.50
      elif atual == 0.50:
        atual = 0.10
      elif atual == 0.10:
        atual = 0.05
      elif atual == 0.05:
        atual = 0.02
      elif atual == 0.02:
        atual = 0.01
      cédulas = 0


   