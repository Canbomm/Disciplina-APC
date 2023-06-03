def trabalhaVetor(lista):
    ocorrenciasPos = {}
    for index,num in enumerate(lista):
        if ocorrenciasPos.get(num) != None:
            ocorrenciasPos[num][0] += 1
        else:
            ocorrenciasPos[num] = [1,index]
    return ocorrenciasPos

tamanho = int(input())
vetor = [int(x) for x in input().split()]
perguntas = int(input())
dicionárioTuplas = trabalhaVetor(vetor)

for _ in range(perguntas):
    x,y = [int(x) for x in input().split()]
    if dicionárioTuplas.get(y) != None:
        print(dicionárioTuplas[y][x-1])
    else:
        print(-1)
