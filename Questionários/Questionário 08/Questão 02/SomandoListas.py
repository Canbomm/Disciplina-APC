quantlistas = int(input()) 
listadelista = []

while quantlistas > 0:
    quantlistas -= 1
    listadelista.append([int(e) for e in input().split()])

indices = [int(e) for e in input().split()]

resposta = listadelista[(indices[0]-1)] + listadelista[(indices[1]-1)]

print(resposta)
