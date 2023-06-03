def vestimentas(chapeus,botas):
    if chapeus > botas:
        total = botas * 2
    elif botas > chapeus:
        total = chapeus * 2
    elif botas == chapeus:
        total = botas * 2
    else:
        total = "Que?"
    print(total)

#essas linhas servem apenas para testar o código
x,y = map(int,input().split())
vestimentas(x,y)
