def positivo(n):
    if n >= 0:
        return True
    else:
        return False

def medianegativa(x):
    # verifica se o primeiro input foi f
    if x == "f":
        print("0.0")
        return ""
    else:   
        acumulador = 0
        cont = 0
        while x != "f":
            x = int(x)
            if not positivo(x):
                cont += 1
                acumulador += x
            x = input()
    # verifica se o cont e 0, caso for, ele nao podera dividir, portanto retorna 0 direto
    if cont == 0:
        print(0.0)
        return ""
    else:
        media_negativo = acumulador/cont
        print(media_negativo)

x = input()
medianegativa(x)
