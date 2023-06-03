inutil = int(input())
lista = [int(x) for x in input().split()]
resposta = "nao"

for num in lista:
    for num2 in lista:
        if (num+num2) == 42:
            resposta = "sim"
            break
print(resposta)
