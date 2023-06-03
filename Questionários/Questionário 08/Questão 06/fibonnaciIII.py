def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        # contando quantas vezes foi feita
        respostas.append(f"fibonacci({numero-1})")
        respostas.append(f"fibonacci({numero-2})")
        # fazendo a sequencia de fibonacci normalmente
        resposta = fibonacci(numero-1) + fibonacci(numero-2)
        return resposta

respostas = []
numero = int(input())
resultado = fibonacci(numero)
# colocando o termo "padrão na lista"
respostas.append(f"fibonacci({numero})")

# contando o total de "fibonaccis"
print(f"Termo: {resultado}")
print("Quantidades:")
for i in range(0,numero+1):
    quantos = 0
    quantos = respostas.count(f"fibonacci({i})")
    print(f"fibonacci({i}) - {quantos}")
