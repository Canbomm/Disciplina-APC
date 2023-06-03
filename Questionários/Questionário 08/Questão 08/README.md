## Não consegui resolver essa questão para todos os casos ##

Durante suas pesquisas, a profa. Vanessa propôs o padrão "apc-2021" para número binários, visando representar números decimais positivos e menores do que 1. Na "apc-2021", o número é representado por uma sequência de 0's e 1's de comprimento arbitrário. Lendo a representação da esquerda para a direita, o primeiro dígito binário representa o valor 2−1, o segundo representa 2−2, o terceiro 2−3, e assim por diante. A representação utiliza sempre o menor número de dígitos possível (ou seja, desta forma o dígito mais à direita é sempre 1).

Por exemplo, a sequência de dígitos binários 012 representa o seguinte valor:

        0*2-1 + 1*2-2 = 0.25

Já a sequência de dígitos binários 1010112 representa o seguinte valor:

        1*2-1 + 0*2-2 + 1*2-3 + 0*2-4 + 1*2-5 + 1*2-6 = 0.671875

Sua tarefa é, dados dois números inteiros X e Y, representados no padrão "apc-2021", determinar a representação da soma X+Y, também no padrão "apc-2021".

## Casos de teste: ##

![Caso que eu não consegui: input1: 6 2, input2: 1 1 0 1 1 1, input3: 1 1](https://i.imgur.com/Yoh9iUF.png "Casos de teste")