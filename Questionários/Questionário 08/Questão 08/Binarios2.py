# tudo errado
def somaApc(padrao1,comp1,padrao2,comp2):
    resposta = []
    if comp1 > comp2:
        maior = comp1
        pmaior = padrao1
        pmenor = padrao2
    else:
        maior = comp2
        pmaior = padrao2
        pmenor = padrao1
    # transformando a menor lista no tamanho da maior
    for i in range(len(pmenor),maior):
        pmenor.append(0)
    for i in range(0,maior):
        soma = pmaior[i] + pmenor[i]
        resposta.append(soma)
    return resposta

comp1, comp2 = map(int,input().split())
padraoapc1 = [int(x) for x in input().split()]
padraoapc2 = [int(x) for x in input().split()]

print(somaApc(padraoapc1,comp1,padraoapc2,comp2))
