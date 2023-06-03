def trabalhaVetor(lista,tamanho):
    ocorrenciasPos = {}
    index = 0
    while index < tamanho:
        num = lista[index]
        if num in ocorrenciasPos:
            ocorrenciasPos[num][0] += 1
        else:
            ocorrenciasPos[num] = [1,index]
        index += 1
    return ocorrenciasPos

tamanho = int(input())
vetor = [int(x) for x in input().split()]
perguntas = int(input())
dicionárioTuplas = trabalhaVetor(vetor,tamanho)

while perguntas > 0:
    x,y = [int(x) for x in input().split()]
    if x == 2:
        print(dicionárioTuplas[y][1])
    else:
        print(dicionárioTuplas[y][0])
    perguntas -= 1
