import math

xCarencio = int(input())
yCarencio = int(input())

xAmor = int(input())
yAmor = int(input())

xDistancia = xAmor - xCarencio
yDistancia = yAmor - yCarencio

distancia = math.sqrt(xDistancia**2 + yDistancia**2)

if distancia <= 100:
    print("É o amor da minha vida!")
elif 100 < distancia <= 200:
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")
