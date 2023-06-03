nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha)
    for i in range(0,len(lido)-1):
        lido[i] = lido[i][:-1]

for linha in lido:
    lista = linha.split(",")
    print(lista[-1])
