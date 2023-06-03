def descomprimestr(string):
    saida = ""
    num = ""
    letra = string[0]
    for char in string[1:]:
        if char.isnumeric():
            num += char
        else:
            saida += (letra*(int(num)))
            letra = char
            num = ""
    saida += (letra*(int(num)))
    return saida

vezes = int(input())
for _ in range(0,vezes):
    entrada = input()
    print(descomprimestr(entrada))
