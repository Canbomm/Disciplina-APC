def não_possui_a_letra_u(palavra):
    for letra in palavra:
        letra = (letra.lower())
        if letra == "u" or letra == "ú" or letra == "ù" or letra == "û" or letra == "ü":
            return False
    return True

# testando valores
""" print(não_possui_a_letra_u("Universidade"))
print(não_possui_a_letra_u("sükûnet"))
print(não_possui_a_letra_u("Baú"))
print(não_possui_a_letra_u("Abobora"))
print(não_possui_a_letra_u("universidade")) """