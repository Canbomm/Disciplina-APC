def tem_letra_maiúscula(s):
    for letra in s:
        if letra.isupper():
            return True
    return False

# testando valores
""" print(tem_letra_maiúscula("Hoje é um novo dia!"))
print(tem_letra_maiúscula("ele disse: Penso, logo existo!"))
print(tem_letra_maiúscula("Achados e perdidos"))
print(tem_letra_maiúscula("achados e perdidos")) """
