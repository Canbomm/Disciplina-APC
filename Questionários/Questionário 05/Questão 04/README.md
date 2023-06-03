Uma série harmônica é uma soma infinita, definida pela seguinte fórmula:
$$\sum_{k=1}^{∞} = 1 + 1/2 + 1/3 + 1/4 + ... $$

Recursivamente, é possível encontrar a soma harmônica dos X primeiros elementos da série, da seguinte forma:

```
soma_harmonica(x) = 1 se x = 1
                    1/x + soma_harmonica(x-1) se x > 1
```

Dessa forma, crie uma função soma_harmonica(X) que calcule recursivamente a soma harmônica de X−1 elementos.