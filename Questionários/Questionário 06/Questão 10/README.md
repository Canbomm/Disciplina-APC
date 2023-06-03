O seguinte programa Python deveria ler uma sequência de números inteiros e parar ao ler o caractere (/f/). Ao final ele deve imprimir a média aritmética dos números negativos da sequência. Depure o programa para que ele funcione corretamente.

```py
def positivo(n):
    if n >= 0:
        return True
    else:
        return False

x = int(input())
acumulador = 0
achou_negativo = False
while x == "f":
    achou_negativo = !positivo(x)
    if achou_negativo:
        cont += 1
        acumulador = acumulador + 1
    x = int(input())
cont += 1
media_negativo = acumulador/cont
print(media_negatvo)
```