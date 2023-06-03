cidadaos = int(input())
gasto = 0

while cidadaos > 0:
    cidadaos -= 1
    salario = int(input())
    if salario < 1000:
        gasto += (1000-salario)
    else:
        pass

print(gasto)