contador = 0
media_turma = 0
lista_media = []
for contador in range(5): # 5 - 1 = 4
    nome = input("Digite o nome do Aluno:")
    media = float(input("Digite a média:"))
    lista_media.append(media)
    media_turma = media_turma + media
media_turma = media_turma / 5
print(lista_media)
print("Parte do for")
for x in lista_media:
    print("A média do aluno é:", x)

print("Parte do while")   
x = 0
while (x < 5):
    print("Média do aluno", lista_media[x])
    x = x +1
    resposta = input("Deseja continuar? (s/n" )
print("A média da turma é:", media_turma)
    