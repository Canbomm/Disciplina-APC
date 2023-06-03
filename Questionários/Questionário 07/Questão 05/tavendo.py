frase = input().split(" ")
contaespaco = 0
# começa no -1 por conta que a primeira e ultima palavra contam como
contapalavra = -1

for palavra in frase:
    if palavra == "":
        contaespaco += 1
    else:
        contapalavra += 1

print(f"Sua frase tem {contaespaco} espaços\nSua frase tem {contapalavra} palavras")
