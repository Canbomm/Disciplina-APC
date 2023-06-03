# O grande problema que eu tive foi contar quando a 'fileira' já começava com 0 ou terminava com 0,
# no final eu só consegui implementar quando começa com 0, por isso lá na frente tem uns reverse loco.
# Mas deu tudo certo :).

def contaespaco(lista):
    conta = 0
    resposta = 0
    if lista[0] == 0:
        for i in lista:
            if i == 1:
                break
            resposta += 2
    for i in lista:
        if i == 1:
            if resposta < conta:
                resposta = conta
            conta = 0
        else:
            conta += 1
    # tratando a resposta
    if resposta % 2 == 0:
        resposta = resposta/2
    else:
        resposta = (resposta + 1)/2
    return int(resposta)

matriz = []
linhas,colunas = map(int,input().split())
linhas_m = linhas

while linhas_m > 0:
    matriz.append([int(x) for x in input().split()])
    linhas_m -= 1

maior = 0
comparacao = 0
for i in range(0,len(matriz)):
    espacos_fileira = contaespaco(matriz[i])
    matriz[i].reverse()
    espacos_fileira_invertido = contaespaco(matriz[i])
    matriz[i].reverse()
    if espacos_fileira > espacos_fileira_invertido:
        comparacao = espacos_fileira
    else:
        comparacao = espacos_fileira_invertido
    if comparacao > maior:
        maior = comparacao

print(maior)
