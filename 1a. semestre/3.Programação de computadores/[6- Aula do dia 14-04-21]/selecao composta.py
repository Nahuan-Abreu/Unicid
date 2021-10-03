#if = se e o else = senão
# usamos quando queremos uma condicao, se a nota for maior ou igual 6 se nao ele é reprovado.
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
n4 = float(input("Digite a quarta nota:"))
ma = (n1+n2+n3+n4)/4
print("A média é:", ma)
if (ma >= 6):
    print("Aluno Aprovado.")
    print("Parabéns.")
else:
    print("Aluno Reprovado.")
    print("Estude Mais.")

    

