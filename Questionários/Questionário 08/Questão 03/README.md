O uso de listas sem os devidos cuidados (e de outros objetos mutáveis) pode levar a longas horas de depuração. Abaixo um programa em Python que usa listas de forma errada. O seguinte programa deveria ler nomes que estão em uma única linha separados por espaços em branco, armazena-los em uma lista e imprimir os nomes que se repetem em ordem alfabética, colocando a quantidade de vezes que aparecem na lista. Depure o programa para fazê-lo funcionar corretamente.

```py
nomes = input().split()
nomes = nomes.sort()
repetido = 0
temp = ""
saida = []
for i in nomes:
    if i == temp:
        repetido += 1
        mudou = True
    else:
        if mudou:
            saida + [temp, repetido]
            repetido = 0
            mudou = False
    temp = i
for i in saida:
    print(i[0], i[1])
```