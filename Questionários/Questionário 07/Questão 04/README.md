Allen B. Downey em seu livro Pense em Python: Pense como um cientista da computação, criou, como exercício, várias funções booleanas para verificar se uma string qualquer possuia pelo menos alguma coisa em particular. Se possuísse, deveria retornas o valor verdadeiro e, caso contrário, o valor falso. A função booleana abaixo deveria retornar verdadeiro sempre que encontrasse uma letra maiúscula na string. Corrija a função para que ela funcione corretamente em qualquer string.

```py
def tem_letra_maiúscula(s):
    for letra in s:
        if not letra.isupper()
            return False
    return True
```