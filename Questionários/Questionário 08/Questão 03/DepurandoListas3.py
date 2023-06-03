nomes = input().split()
nomes.sort()
# como o código se baseia comparando o ultimo elemento com o proximo, eu precisei adicionar esse elemento aleatório para fazer com que ele rode mais uma vez
nomes.append("Esse elemento nunca será lido")

repetido = 1
temp = ""
saida = []
mudou = False

for i in nomes:
    if i == temp:
        repetido += 1
        mudou = True
    else:
        if mudou:
            saida += [temp, repetido]
            repetido = 1
            mudou = False
    temp = i

for i in range(0,len(saida),2):
    print(saida[i], saida[i+1])