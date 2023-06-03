frase = input().split()
nome_arq = frase[-1]

try:
    with open(nome_arq) as arquivo:
        lido = []
        for linha in arquivo:
            lido.append(linha.rstrip())
    print(f"da pra abrir")
    tuplas = []
    for linha in lido:
        nome,pontos = linha.split()
        pontos = int(pontos)
        tuplas.append((nome,pontos))
    tuplas = sorted(tuplas, key=lambda tupla: tupla[1], reverse=True)
    for tupla in tuplas:
        print(tupla)
except:
    print(f"nao da pra abrir")
