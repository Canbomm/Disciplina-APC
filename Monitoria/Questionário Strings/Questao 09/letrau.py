def não_possui_a_letra_u(palavra):
    palavra = palavra.lower()
    for letra in palavra:
        if letra == "u" or letra == "ú" or letra == "ù" or letra == "û" or letra == "ü":
            return False
    return True

print(não_possui_a_letra_u("Universidade"))
print(não_possui_a_letra_u("sükûnet"))
print(não_possui_a_letra_u("Baú"))
print(não_possui_a_letra_u("Nao posso ter a letra proibida"))
