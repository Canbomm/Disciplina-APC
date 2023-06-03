def comprarCelular():
    colegasCelular = {}
    apareceCelular = {}
    for _ in range(4):
        # inputs
        nomeColega = input()
        modelo = input()
        preco = int(input())
        # fazendo o dic
        colegasCelular[nomeColega] = (modelo,preco)
        # vendo a repeticao
        repete = True
        if apareceCelular.get(modelo) != None and repete:
            apareceCelular[modelo] += 1
        else:
            apareceCelular[modelo] = 1
    maisAparece = 0
    for chave in apareceCelular:
        apareceAtual = apareceCelular[chave]
        if apareceAtual > maisAparece:
            maisAparece = apareceAtual
            candidato = chave
    return candidato

def desempate(dicCelulares):
    menor = float('inf')
    for chave in dicCelulares:
        modelo,preco = dicCelulares[chave]
        if preco < menor:
            menor = preco
            modeloEscolhido = modelo
    return modeloEscolhido

print(comprarCelular())