# resultado = 1° * 2 + 2° * 1/2
# resultado*2

lista = [int(x) for x in input().split()]
if len(lista) > 2:
    soma = ((lista[0]*2) + (lista[1]*(1/2))) * 2
else:
    soma = 0

for ind in range(2,len(lista)):
    soma += (lista[ind] * (1/2))
    soma *= 2

print(f"{soma/2:.2f}")
