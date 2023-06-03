def contaelemento(lista,elemento):
    conta = 0
    for e in lista:
        if e == elemento:
            conta += 1
    return conta

lista = [int(e) for e in input().split()]
quantTestes = int(input())
total_e = 0

while quantTestes > 0:
    quantTestes -= 1
    elemento, vezes = map(int,input().split())
    quantos = contaelemento(lista,elemento)
    if quantos == 0:
        print(f"{elemento} nao esta na lista")
    else:
        if quantos == vezes:
            print(f"tudo ok")
        else:
            falta = vezes - quantos
            lista += ([elemento]*falta)
            lista.sort()
            print(*lista)
