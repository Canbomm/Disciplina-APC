É muito comum em programação usarmos operadores lógicos. Python fornece 3 operadores lógicos: not, and e or. Esses três são suficientes para descrever qualquer expressão lógica, mas não são os únicos que existem.

Um outro operador lógico que existe é o condicional. Sejam p e q expressões lógicas, a operação condicional p→q é definida de acordo com a tabela verdade abaixo.

```
p | q | p → q
---------------
V | V |   V
V | F |   F
F | V |   V
F | F |   V
```
Seu trabalho será implementar a operação lógica condicional, mas para 3 expressões. Para isso, implemente uma função cond, que recebe os argumentos p, q e r (booleanos), e retorne o resultado de p→q→r. Obs.: condicional é uma operação left-associative, ou seja, p→q→r é a mesma coisa que (p→q)→r.