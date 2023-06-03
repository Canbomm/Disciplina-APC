# não funciona em todos os casos
def interpretaAPC(lista):
    resp = 0
    conta = -1
    for e in lista:
        resp += (e * 2**(conta))
        conta -= 1
    return resp

def codificaAPC(num,casas):
    resposta = [0]*casas
    index = casas-1
    while index > -1:
        resposta[index] = 1
        teste = interpretaAPC(resposta)
        # verificar se a resposta deu maior
        if (str(teste)[2:])[index] > (str(num)[2:])[index]:
            resposta[index] = 0
        index -= 1
    return resposta

comp1, comp2 = map(int,input().split())
padraoapc1 = [int(x) for x in input().split()]
padraoapc2 = [int(x) for x in input().split()]

# decodificando
apc1_dec = interpretaAPC(padraoapc1)
apc2_dec = interpretaAPC(padraoapc2)
soma_num = apc1_dec + apc2_dec

# codificando
casas = len((str(soma_num))[2:])
resposta = codificaAPC(soma_num,casas)
print(*resposta)
