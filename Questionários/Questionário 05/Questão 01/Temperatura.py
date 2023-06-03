def converter(temp,tipo):
    if tipo == "C":
        tempfinal = (temp * 1.8) + 32
    elif tipo == "F":
        tempfinal = 0.5555556 * (temp - 32)
    else:
        print("Entrada inválida")
    return tempfinal

# Testando pra ver se está tudo certo
# print(converter(180, 'C'))
