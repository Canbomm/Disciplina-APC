amigos,preco = input().split()
preco = int(preco)
amigos = int(amigos)

dinheiro_total = 0
parada = 0

while parada < amigos:
    dinheiro = int(input())
    dinheiro_total += dinheiro
    parada += 1

if amigos > 0:
    media = int(dinheiro_total/amigos)
else:
    media = 0

print(f"media: {media}")
if media >= preco:
    print("o rock reinara mais uma vez")
else:
    print("rockeiros trabalhando ja")
