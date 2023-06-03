A princesa e o dragão
Uma história muito conhecida e bem clichê é a da princesa no quarto mais alto da torre mais alta guardada por um dragão. E geralmente tem um cavaleiro no meio, e essa não é diferente.

Temos uma imagem da torre onde estão a princesa (no quarto mais alto), um cavaleiro correndo por sua vida para chegar até a princesa, e um dragão com fome. Essa imagem está em um arquivo de texto como o exemplo abaixo

```
|¯|_|¯|_|¯|_|¯|_|¯|
|             P   |
|-----------------|
|                 |
|-----------------|
|       C         |
|-----------------|
|                 |
|-----------------|
|                 |
|-----------------|
|        D        |
###################
```

Veja que a princesa está no andar 6, o cavaleiro no andar 4 e o dragão no andar 1.

A torre sempre possui essa largura, e os andares são sempre desta forma, mas o tamanho da torre (quantidade de andares) pode ser diferente.

Além disso, o cavaleiro consegue subir 1 andar por vez, mas o dragão consegue subir 2 andares por vez. Como cavaleiros correndo atrás de princesas são uma ocasião cada vez mais rara o dragão ficou animado e disse alguma coisa no final da história, ou ele disse "Quero ver descerem u.u" - se o cavaleiro conseguiu chegar até a princesa - ou então "Mais um pro lanche!" - se ele conseguiu chegar ao cavaleiro antes.

O seu trabalho é dizer o que acontece nessa história.

## Entrada ##

A entrada do programa consiste de uma linha contendo o nome do arquivo txt a ser lido. Ele é formatado conforme mostrado acima, com a imagem da torre.

É garantido que haverá uma princesa P, um cavaleiro C e um dragão D na torre. Eles estarão dentro de algum andar da torre (as linhas com espaços).

## Saida ##

Você deve imprimir 4 linhas. 

A primeira linha deve ser "Princesa no andar ap", onde ap é o andar da princesa.

A segunda linha deve ser "Cavaleiro no andar ac", onde ac é o andar do cavaleiro.

A terceira linha deve ser "Dragão no andar ad", onde ad é o andar do dragão.

A quarta linha deve ser a frase que o dragão diz no final da história. Se o dragão consegue chegar até o mesmo andar que o cavaliro, ou até um andar acima do cavaleiro antes que o cavaleiro chegue no andar da princesa, ele diz "Mais um pro lanche!". Se eles chegarem no último andar juntos então o cavaleiro vence, porque o dragão nunca entra no quarto da princesa. Se o cavaleiro chegar no quarto da princesa primeiro, ele diz "Quero ver descerem u.u"
