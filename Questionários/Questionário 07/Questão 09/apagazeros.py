codigo = input()
contador = 0
percorreu = 0
resposta = 0

for c in codigo:
    c = int(c)
    if c == 1:
        if contador > 1 and percorreu > codigo.find("1"):
            resposta += (contador - 1)
        contador = 0
    contador += 1
    percorreu += 1

print(resposta)
