palavra = input()

for letra in palavra:
    # ele nao quer que duplique os espacos
    if letra != " ":
        print(f"{letra} ",end="")
