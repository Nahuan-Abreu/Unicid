cigarros = float(input("Digite a quantidade de cigarros que você fuma por dia: ")) 
anos = float(input("Digite ah quantos anos você fuma: "))  
total_de_cigarros = (anos * 365) * cigarros
total_de_dias_perdido = (total_de_cigarros * 10)/24
print("Você perdeu", total_de_dias_perdido,"dias de vida")