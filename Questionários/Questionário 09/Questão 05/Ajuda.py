def achaVetor(lista,numero):
    try:
        posicao = lista.index(numero)
    except:
        posicao = -1
    return posicao

def quantasOcorrencias(lista):
    ocorrencias = {}
    for num in lista:
        if num in ocorrencias:
            ocorrencias[num] += 1
        else:
            ocorrencias[num] = 1
    return ocorrencias

tamanho = int(input())
vetor = [int(x) for x in input().split()]
perguntas = int(input())
ocorrencias = quantasOcorrencias(vetor)

while perguntas > 0:
    x,y = [int(x) for x in input().split()]
    if x == 2:
        print(achaVetor(vetor,y))
    else:
        print(ocorrencias[y])
    perguntas -= 1
