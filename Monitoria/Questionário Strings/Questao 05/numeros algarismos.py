entrada = input().split()
saida = ""
for pal in entrada:
    if pal == "um":
        saida += "1 "
    elif pal == "dois":
        saida += "2 "
    elif pal == "três":
        saida += "3 "
    elif pal == "quatro":
        saida += "4 "
    elif pal == "cinco":
        saida += "5 "
    elif pal == "seis":
        saida += "6 "
    elif pal == "sete":
        saida += "7 "
    elif pal == "oito":
        saida += "8 "
    elif pal == "nove":
        saida += "9 "
    else:
        saida += (pal + " ")
print(saida)
