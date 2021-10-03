#usamos o elif quando queremos dar mais de uma condicao como no exemnplo, temos 3, 1- se a nota for mais ou igual a 6, 2= se a nota for entre 3 e 6, 3- se a nota for menor que 3 
n1 = float(input("Digite a primeira nota:"))
if n1 < 0:
    print("erro")
n2 = float(input("Digite a segunda nota:"))
if n2 < 0:
    print("erro")
n3 = float(input("Digite a terceira nota:"))
if n3 < 0:
    print("erro")
n4 = float(input("Digite a quarta nota:"))
if n4 < 0:
    print("erro")
ma = (n1+n2+n3+n4)/4
print("A média é:", ma)
if (ma >= 6):
    print("Aluno Aprovado.")
    print("Parabéns.")
elif (ma < 6 and ma >3)
    print("Aluno de Exame.")
elif (ma < 3):
    print("Aluno Reprovado.")
    print("Estude Mais.")
else:
    print("Seu usuário Idiota, você digitou valores absurdos!")
    
