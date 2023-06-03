frase = input()
contador,resposta = -2,0

for c in range(0,len(frase)):
    # fazendo a soma
    if frase[c] == " ":
        if frase[c-1] != " ":
            contador = -2
        contador += 1
    # pegando a resposta
    if frase[c] == " " and frase[c+1] != " ":
        resposta = contador
        if resposta >= 0:
            print(resposta)
        else:
            resposta = 0
            print(resposta)
# nao me orgulho muito desse codigo mas ele funciona