def dinheiros(desejado,preco1l,preco2l):
    if preco1l * 2 <= preco2l:
        # compensa mais comprar de 1l em 1l
        valor = desejado * preco1l
    else:
        # compensa mais comprar 2l de uma vez
        falta = desejado % 2
        valor = ((desejado-falta)/2) * preco2l + falta * preco1l
    valorfinal = int(valor)
    print(valorfinal)
