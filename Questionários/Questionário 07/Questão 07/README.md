Allen B. Downey em seu livro Pense em Python: Pense como um cientista da computação, fala da dificuldade em se testar programas. Em particular sobre strings ele diz que:

* "As funções no Capítulo de Strings e Estudo de caso: jogos de palavras  são relativamente fáceis para testar porque é possível verificar os resultados à mão. Ainda assim, pode ser difícil ou até impossível escolher um grupo de palavras que teste todos os erros possíveis." 

Dito isto, corrija o código da seguinte função que dado uma palavra retorna Verdadeiro se ela não possui a letra (/u/) e Falso se possuir a letra (/u/).

```py
def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if not letra==u:
            return False
    return True
```