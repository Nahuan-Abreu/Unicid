divida = float(input('valor da divida: '))
juros = float(input('valor dos juros mensal: '))
meses = float(input('quanto sera pago por mes: '))
total = divida + (divida * juros)
juros = total - divida
quatidade_de_meses = total / meses
print("-----------------------------------  ")
print(f"número de meses para que a divida seja paga: {quatidade_de_meses}")
print(f"total pago: {total}")
print(f"total de juros pago: {juros}")