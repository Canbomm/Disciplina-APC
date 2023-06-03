def naoAosCentavos(compra,parcelas,afiliado):
    if compra >= 350:
        # promocao especial dessa semana
        pague = compra % parcelas
        pagueint = int(pague)
        print(f"Eba! Você ganhou {pagueint} reais de desconto!")
    else:
        if afiliado == 1:
            # nao e afiliado
            pague = compra % parcelas
            pagueint = int(pague)
            print(f"Eba! Você ganhou {pagueint} reais de desconto!")
        elif afiliado == 0:
            # e afiliado
            pague = compra % parcelas
            pagueint = int(pague)
            print(f"Por favor, pague {pagueint} reais para prosseguir com o parcelamento")
        else:
            # input errado pelo usuario
            print("Por favor....")

compra,parcelas,afiliado = map(float,input("").split(" "))
naoAosCentavos(compra,parcelas,afiliado)
