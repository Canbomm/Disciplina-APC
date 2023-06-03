n = int(input())
contador, percorreu, resposta = 0,0,0

while n > 0:
    codigo = input()
    contador, percorreu, resposta = 0,0,0
    for c in codigo:
        c = int(c)
        if c == 1:
            if contador > 1 and percorreu > codigo.find("1"):
                resposta += (contador - 1)
            contador = 0
        contador += 1
        percorreu += 1
    print(resposta)
    n -= 1
