informacoes = {}

for _ in range(4):
    nome = input()
    modelo = input()
    valor = int(input())
    if informacoes.get(modelo) != None:
        informacoes[modelo] += [valor]
    else:
        informacoes[modelo] = [valor]

def contaModelos(info):
    for chave in info:
        quantos = len(info[chave])
        info[chave] = [quantos] + info[chave]
    return info

def escolheModelo(info):
    maior = 0
    menor = float('inf')
    for chave in info:
        quantidade = info[chave][0]
        if quantidade > maior:
            maior = quantidade
            candidatoModelo = chave
            precos = info[chave][1:]
            for preco in precos:
                if preco < menor:
                    menor = preco
                    candidatoModelo = chave
        elif quantidade == maior:
            precos = info[chave][1:]
            for preco in precos:
                if preco < menor:
                    menor = preco
                    candidatoModelo = chave
    return candidatoModelo

print(escolheModelo(contaModelos(informacoes)))
