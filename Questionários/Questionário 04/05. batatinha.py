import math

def brincaComGato(distanciamax,cgato1,cgato2,cbola1,cbola2):
    distancia = math.sqrt((cbola1-cgato1)**2 + (cbola2-cgato2)**2)
    if distancia < distanciamax:
        print("*miau* ta bom, vou buscar")
    elif distancia == distanciamax:
        print("pfff... ta bom")
    else:
        print("ta achando que eu sou cachorro?")

distanciamax = float(input())
coordenadagato1 = float(input())
coordenadagato2 = float(input())
coordenadabola1 = float(input())
coordenadabola2 = float(input())
brincaComGato(distanciamax,coordenadagato1,coordenadagato2,coordenadabola1,coordenadabola2)
