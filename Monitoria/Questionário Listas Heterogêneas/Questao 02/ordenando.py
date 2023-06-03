# esse codigo nao funciona para todos os casos

totalListas = int(input())
indiceOrdena = int(input())

matriz = []
for i in range(0,totalListas):
    matriz.append([int(x) for x in input().split()])

# ordenando as listas com base no indice
elementos = []
for lista in matriz:
    elementos.append(lista[indiceOrdena])
elementos.sort()

# pegando os elementos em ordem
matrizordenada = []
elementosindex = 0
index = 0
while matriz:
    resetaindex = False
    if matriz[index][indiceOrdena] == elementos[elementosindex]:
        matrizordenada.append(matriz.pop(index))
        elementosindex += 1
        resetaindex = True
    # resetando o index caso ele tenha encontrado
    if resetaindex:
        index = 0
    else:
        index += 1

# printando a matriz ordenada
for linha in matrizordenada:
    print(linha)
