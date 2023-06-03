# so copiei o codigo que eu ja tinha feito na questao 07
def não_possui_a_letra_u(palavra):
    for letra in palavra:
        letra = (letra.lower())
        if letra == "u" or letra == "ú" or letra == "ù" or letra == "û" or letra == "ü":
            return False
    return True