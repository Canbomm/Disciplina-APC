def conta_espaco(lista):
    contagem = 0
    maior_espaco = 0
    # caso comece com 0
    if lista[0] == 0:
        for num in lista:
            if num == 1:
                break
            # de dois em dois pq eu vou dividir por 2 no final
            contagem += 2
        # guardando o espaco inicial
        if contagem > maior_espaco:
            maior_espaco = contagem
        contagem = 0
    # caso termine com 0
    if lista[-1] == 0:
        for num in lista[::-1]:
            if num == 1:
                break
            # mesma coisa do anterior
            contagem += 2
        # guardando o espaco final
        if contagem > maior_espaco:
            maior_espaco = contagem
        contagem = 0
    # caso geral
    for num in lista:
        if num == 0:
            contagem += 1
        else:
            if contagem > maior_espaco:
                maior_espaco = contagem
            contagem = 0
    # arredondando pra cima
    maior_espaco = arredonda(maior_espaco/2)
    return maior_espaco

def arredonda(num):
    resto = num % 1
    if resto == 0:
        return int(num)
    else:
        if resto >= 0.5:
            return int((num - resto) + 1)
        else:
            return int((num - resto))

print(conta_espaco([0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1]))
print(conta_espaco([0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1]))
