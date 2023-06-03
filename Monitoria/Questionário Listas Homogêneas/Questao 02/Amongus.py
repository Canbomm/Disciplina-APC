jogadores = []
for _ in range(0,int(input())):
    jogadores.append(input())
impostores = input().split()

inocentes = []
for jogador in jogadores:
    if not jogador in impostores:
        inocentes.append(jogador)
print(" ".join(inocentes))
