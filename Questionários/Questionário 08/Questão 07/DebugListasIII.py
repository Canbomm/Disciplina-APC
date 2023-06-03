def mediana_e_mais_proximo_media_e_pos(lista):
    # mudei para não acontecer o caso dos "ponteiros"
    lista2 = lista[:]
    lista2.sort()
    tam = len(lista2)
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista2[int(tam/2)] + lista2[int(tam/2-1)])/2
        else:
            mediana = (lista2[int(tam/2)])
        somador = 0
        for i in lista:
            somador += i
        media = somador/tam
        delta = lista2[tam-1] - lista2[0]
        prox_media = lista2[0]
        index=0
        # também mudei essa parte pra pegar o index correto
        for i in range(len(lista)):
            if abs(media-lista[i]) < delta:
                prox_media = lista[i]
                index = i
                delta = media - lista[i]
    else:
        prox_media = None
        mediana = None
        index = None
    return mediana, prox_media, index

# testando
lista = [1, 2, 3, 4]
print(mediana_e_mais_proximo_media_e_pos(lista))

lista = [1, 1, 1, 1, 1, 1, 1, 50, 43, 0]
print(mediana_e_mais_proximo_media_e_pos(lista))

lista = []
print(mediana_e_mais_proximo_media_e_pos(lista))
