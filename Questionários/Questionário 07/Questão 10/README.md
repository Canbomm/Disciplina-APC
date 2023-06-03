Segundo o lendário cientista da computação Edsger W. Dijkstra:

* "Testar programas pode ser usado para mostrar a presença de bugs, mas nunca para mostrar a ausência deles! "

Dito isto, deixe o código mais correto possível na seguinte função que dado uma string retorna Verdadeiro se ela não possui a letra (/u/) e Falso se possuir a letra (/u/).

```py
def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if not letra==u:
            return False
    return True
```