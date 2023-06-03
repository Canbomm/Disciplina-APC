lista = [int(x) for x in input().split()]
lista2 = [1,0,0,0,0,0,1]

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

normal = contaespaco(lista)
lista.reverse()
invertida = contaespaco(lista)
lista.reverse()

if normal > invertida:
    resposta = normal
else:
    resposta = invertida

print(resposta)