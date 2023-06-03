import sys
sys.setrecursionlimit(10**6)

tamanho = int(input())
lista = [int(x) for x in input().split()]
dicFibo = {"fibonacci(0)":0,"fibonacci(1)":1}

def fibonacci(numero):
    if dicFibo.get(f"fibonacci({numero})") != None:
        return dicFibo.get(f"fibonacci({numero})")
    else:
        resposta = fibonacci(numero-1) + fibonacci(numero-2)
        dicFibo[f"fibonacci({numero})"] = resposta
        return resposta

respostas = []
for num in lista:
    respostas.append(fibonacci(num-1))
print(tuple(respostas))
