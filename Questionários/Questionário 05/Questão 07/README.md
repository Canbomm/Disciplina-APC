O código abaixo é a implementação de duas funções. A função calcula_delta recebe os coeficientes a, b e c de uma função do segundo grau (a×x2+b×x+c) e o valor de x. Após o cálculo do delta, caso esse não seja negativo, é calculado o valor numérico da função a partir de x pela função calcula_f.

```py
def calcula_f(a,b,c,x):
  print((a*x*2)+(b*x)+c)

def calcula_delta(a,b,c,x):
  delta = (b*b - 4*a*c)
  if(delta < 0):
    return "Equacao sem raizes reais"
  else:
    return "O resultado de f(" + x + ") eh: " + str(calcula_f(a,b,c,x)) 
```

A partir dos exemplos disponibilizados, identifique os erros que o código acima apresenta e faça os ajustes necessários para que funcione de maneira correta.