Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência: 

0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...  

Após dominar o uso de funções recursivas envolvendo fibonacci, Charlinho ficou com uma pergunta na cabeça: "Quantas vezes cada chamada para a função fibonacci é realizada para cada número menor que n?" Para ajudar a responder a essa pergunta, ele resolveu desenhar uma estratura que parece uma árvore de ponta cabeça com as quantidades de chamadas, e ela ficou da seguinte forma:

![Representação Fibonacci](https://imgur.com/zZeStI4.png "Árvore de 'sequências de Fibonacci'")

Perceba que na árvore, Charlinho coloca no topo o valor que deseja calcular (Fibonacci de 4). Essa chamada gera outras duas chamadas para Fibonnaci de 2 e 3. A chamada de Fibonacci de 2 gera as chamadas de Fibonacci de 1 e 0 enquanto a chamada de Fibonacci de 3 geram as chamadas de Fibonacci de 2 e 1. Por fim, a chamada de Fibonacci de 2 geram as chamadas de Fibonacci de 1 e 0.

Para não precisar sempre desenhar essa árvore, ele pediu a sua ajuda para implementar um programa que conte quantas vezes cada chamada da função fibonacci é realizada, para cada valor de entrada diferente da função recursiva. Observe que, ao elaborar seu programa, você deve definir uma função fibonacci que recebe como parâmetro um número inteiro n fornecido da entrada padrão, e considerá-la na resolução do problema.
