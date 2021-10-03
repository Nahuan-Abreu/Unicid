#selecao encadeada é quando usamos if dentro de if e else como no exemplo abaixo que  temos um if e else e dentro deles temos mais um if e else assim fazendo uma selecao cadeada
#usamos a encadeada quando queremos ter apenas duas condicoes, como no exemplo abaixo, temos a primeira se a nota for maior ou igual a 6, e a segunda se a nota estiver entre 3 e 6.
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
    if (ma < 6 and ma >= 3):
        print("Aluno de Exame.")
    else: 
        print("Aluno Reprovado.")
        print("Estude Mais.")
