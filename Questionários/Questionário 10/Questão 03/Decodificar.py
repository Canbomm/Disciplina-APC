nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha.rstrip())

for codigo in lido:
    index = 0
    resposta = ""
    numero = ""
    for caractere in codigo:
        if caractere.isdecimal():
            numero += caractere
        else:
            if numero != "":
                resposta += codigo[index-len(numero)-1]*(int(numero)-1)
                numero = ""
            resposta += caractere
        index += 1
    if numero != "":
        resposta += codigo[index-len(numero)-1]*(int(numero)-1)
        numero = ""
    print(resposta)
