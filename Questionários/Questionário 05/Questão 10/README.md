A sequência de Collatz modificada é formada da seguinte forma: Dada uma semente inicial s, o próximo número da sequência é n/2 se n é par e 3n−1 do contrário.  Collatz, que está aprendendo programação, implementou uma função recursiva para achar o n-ésimo termo da sua sequência. 

```py
def collatz(s, n, cont):
    if cont <= n:
        if s % 2 == 0: #é par
            clltz = int(s/2)
        else:
            clltZ = 3*s - 1
        collatz(clltz, n, cont+1)
    else:
        return s
```

Mas a função dele contém erros de sintaxe e lógica. Ajude-o a depurar o código Python da função collatz.