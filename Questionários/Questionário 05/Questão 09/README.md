O máximo divisor comum (MDC) entre dois ou mais números inteiros é o maior número inteiro que é fator de todos eles. Por exemplo, os divisores comuns de 12 e 18 são 1, 2, 3 e 6, logo o mdc(12,18)=6. No ano 300 a.c., o livro Elementos descreve um método para encontrar o MDC de dois números que é utilizado até os dias atuais, e é conhecido como Algoritmo de Euclides. Esse método baseia-se na seguinte propriedade: mdc(a,b)==mdc(b,r), onde r é o resto da divisão de a por b.
Dessa forma, aproveitando-se dessa propriedade, é possível realizar sucessivas divisões entre pares de valores e seus restos, até que o resto de alguma divisão seja zero. Quando o resto passa a ser zero, o segundo elemento do último mdc realizado é o MDC dos pares iniciais. O algoritmo funciona da seguinte maneira:

```py
mdc(32,26) - Resto da divisão de 32 por 26 é 6
mdc(26,6) - o resto da divisão de 26 por 6 é 2
mdc(6,2) - o resto da divisão de 6 por 2 é 0
mdc(2,0) - o resultado é 2, para mdc(32,26)
```

Dessa forma, é possível escrever um algoritmo recursivo para o método de euclides da seguinte forma:
```
mdc(a,b) = a            se b = 0
           mdc(b,a%b)   se a%b > 0,b > 0
```

Dada a especificação recursiva para o algoritmo de euclides, sua tarefa é implementar uma função ;mdc(a, b) que calcule o MDC entre dois números a e b.