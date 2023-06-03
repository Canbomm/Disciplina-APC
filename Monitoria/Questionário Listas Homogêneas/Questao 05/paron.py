def paron(lista):
    vogais_pares = []
    for palavra in lista:
        vogais = 0
        for char in palavra:
            char = char.lower()
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                vogais += 1
        if vogais % 2 == 0:
            vogais_pares.append(palavra)
    return vogais_pares
