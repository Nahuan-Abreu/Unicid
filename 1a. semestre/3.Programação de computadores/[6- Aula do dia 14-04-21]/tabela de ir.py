#and = Usamos o "e" quando queremos "e" dizer 5 e 7. Usamos o or quando queremos usaro "ou", como, 5 ou 7. and = e, or = ou 
# selecao = if 
#repeticao = while / fpr
#combinacao =  while + if e else
salario = float(input("Digite o salário para cálculo do imposto: "))
qtde_dependente = int(input("Digite a quantidade de dependentes:"))
if (salario <= 22847.76):
  print("Não precisará pagar o IRPF. - Nada a Deduzir")
elif (salario <= 33919.80):
  print("Alíquota: 7,5%. Dedução: 1.713,58")
elif (salario <= 45012.60):
  print("Alíquota: 15%. Dedução: 4.257,57")
elif (salario <= 55976.16):
  print("Alíquota: 22,5%. Dedução: 7.633,51")
else:
  print("Alíquota: 27,5%. Dedução: 10.432,32")
print("A parcela por dependente é:", qtde_dependente * 189.59)
 