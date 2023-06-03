O uso de listas sem os devidos cuidados (e de outros objetos mutáveis) pode levar a longas horas de depuração. Abaixo uma função em Python que usa listas de forma errada. A função deveria receber como parâmetro uma lista com números reais e retornar como resultado uma lista contendo o valor da mediana, do elemento da lista que é o mais próximo da média aritmética, e a posição desse elemento na lista (seu índice) - nesta ordem.  Depure a função para fazê-la funcionar corretamente.

```py
def mediana_e_mais_proximo_media_e_pos(lista):
    lista = lista.sort()
    tam = len(lista)
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista[int(tam/2)] + lista[int(tam/2-1)])/2
        else:
            mediana = (lista[int(tam/2)])
        somador = 0
        for i in lista:
            somador += i
        media = somador/tam
        delta = lista2[tam-1] - lista2[0]
        prox_media = lista[0]
        index=0
        for i in lista:
            if abs(media-i) < delta:
                prox_media = i
                index = i
                delta = media - i
    else:
        prox_media = None
        mediana = None
        index = None
    return mediana, prox_media, index
```
