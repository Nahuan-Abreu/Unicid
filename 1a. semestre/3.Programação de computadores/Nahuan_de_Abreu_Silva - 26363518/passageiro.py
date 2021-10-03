distancia = float(input("Digite a distancia em km que seja percorre:"))
if distancia <= 200:
    preço1=distancia*0.50
    print("O valor da possagem será:",preço1, "Reais")
else:
    preço2 = distancia*0.45  
    print("O valor da possagem será:",preço2, "Reais")     
    