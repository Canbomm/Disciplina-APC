def pegaInput():
    repeticao = 5
    lista = []
    while repeticao > 0:
        valor = int(input())
        lista.append(valor)
        repeticao -= 1
    return lista

lista1 = pegaInput()
lista2 = pegaInput()

list_tuple = list(zip(lista1,lista2))
print(list_tuple)

medias = []
for tupla in list_tuple:
    media = (tupla[0] + tupla[1])/2
    medias.append(media)

print(medias)
