O uso de listas sem os devidos cuidados (e de outros objetos mutáveis) pode levar a longas horas de depuração. Abaixo uma função em Python que usa listas de forma errada. A função deveria receber como parâmetro uma lista com números reais e retornar como resultado o valor da mediana, o elemento da lista que é o mais próximo da média aritmética bem como sua posição na lista. A posição da lista é o seu índice na lista. Depure a função para fazê-la funcionar corretamente.

```py
def mediana_e_mais_proximo_media_e_pos(lista):
    lista2 = lista
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
        for i in range(len(lista2)):
            if abs(media-lista2[i]) < delta:
                prox_media = lista2[i]
                index = i
                delta = media - lista2[i]
    else:
        prox_media = None
        mediana = None
        index = None
    return mediana, prox_media, index
```