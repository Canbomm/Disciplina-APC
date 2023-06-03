# muito pesado não consegue calcular o fibo de 1000
import sys
sys.setrecursionlimit(10**6)

tamanho = int(input())
lista = [int(x) for x in input().split()]

def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        resposta = fibonacci(numero-1) + fibonacci(numero-2)
        return resposta

respostas = []
for num in lista:
    respostas.append(fibonacci(num-1))
print(tuple(respostas))
