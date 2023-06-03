numeros = [int(x) for x in input().split()]
divisor = int(input())

divisores = []
for num in numeros:
    if num % divisor == 0:
        divisores.append(str(num))

print(" ".join(divisores))
