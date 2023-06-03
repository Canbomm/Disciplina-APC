def verificadiagonais(matriz):
    # pegando os indices das diagonais
    posincial = 0
    posfinal = len(matriz[0])-1

    # percorrendo a matriz
    for linha in matriz:
        index = 0
        for coluna in linha:
            # se o caractere em questao faz parte de uma diagonal
            if index == posincial or index == posfinal:
                if coluna != "X":
                    return False
            # se nao faz parte, ele nao pode ser X
            elif coluna == "X":
                return False
            index += 1
        # atualizando os "indices das diagonais"
        posincial += 1
        posfinal -= 1
    # caso percorra tudo sem dar false, e poneglifo
    return True

# pegando a entrada
tamanhoMatriz = int(input())
matriz = []
while tamanhoMatriz > 0:
    matriz.append(input().split())
    tamanhoMatriz -= 1

# vendo se ela possui X nas diagonais
poneglifo = verificadiagonais(matriz)

if poneglifo:
    print("O one piece eh real!")
else:
    print("Talvez o tesouro seja os amigos que fizemos no caminho")
