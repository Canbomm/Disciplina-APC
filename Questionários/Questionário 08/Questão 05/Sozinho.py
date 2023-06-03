def contaelemento(lista,elemento):
    conta = 0
    for e in lista:
        if e == elemento:
            conta += 1
    return conta

# não usei essa variável para nada
quantmeias = int(input())

meias = [int(x) for x in input().split()]

for e in meias:
    epar = contaelemento(meias,e)
    if epar == 1:
        print(f"{e} sozinho")
        break
