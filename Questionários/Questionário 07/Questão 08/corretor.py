frase = input()
corrigida = ""

for letra in frase:
    if letra == "9":
        corrigida += "p"
    elif letra == "6":
        corrigida += "b"
    elif letra == "5":
        corrigida += "s"
    elif letra == "7":
        corrigida += "t"
    elif letra == "0":
        corrigida += "o"
    elif letra == "1":
        corrigida += "i"
    else:
        corrigida += letra
    
# corrige as letras maisculas
final = corrigida.lower()
final = final[0].upper() + final[1:]

# adiciona o ponto final
if final[-1] != ".":
    final += "."

print(final)
