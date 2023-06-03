# muita sacanagem botarem um caso em que dois personagens estão no mesmo andar

lido = ["|¯|_|¯|_|¯|_|¯|_|¯|",
"|            P    |",
"|-----------------|",
"|                 |",
"|-----------------|",
"|                 |",
"|-----------------|",
"|         D C     |",
"###################"]

topo = lido.pop(-1)
fundo = lido.pop(0)

personagens = {"C":"Cavaleiro","P":"Princesa","D":"Dragão","E":"Error"}

def procuraTudo(string):
    pPri = string.find("P")
    pCav = string.find("C")
    pDrag = string.find("D")
    if pPri != -1 or pCav != -1 or pDrag != -1:
        perso1, perso2, perso3 = " ", " ", " "
        if pPri != -1:
            perso1 = personagens[string[pPri]]
        if pCav != -1:
            perso2 = personagens[string[pCav]]
        if pDrag != -1:
            perso3 = personagens[string[pDrag]]
        return True, perso1, perso2, perso3
    else:
        return False, "E"

andar = 1
posicoes = {}
for linha in lido[::-1]:
    if linha != "|-----------------|":
        procurando = procuraTudo(linha)
        if procurando[0]:
            for personagem in procurando[1:]:
                if personagem != " ":
                    posicoes[personagem] = [(f"{personagem} no andar {andar}"), andar]
        andar += 1

print(posicoes["Princesa"][0])
print(posicoes["Cavaleiro"][0])
print(posicoes["Dragão"][0])

def simulaJogo(posicoes):
    if (posicoes["Cavaleiro"][1]) == (posicoes["Princesa"][1]):
        return("Quero ver descerem u.u")
    elif (posicoes["Dragão"][1]) >= (posicoes["Cavaleiro"][1]):
        return("Mais um pro lanche!")
    else:
        return("O jogo continua")

comeco = simulaJogo(posicoes)
if comeco != "O jogo continua":
    print(comeco)
else:
    while simulaJogo(posicoes) == "O jogo continua":
        posicoes["Cavaleiro"][1] += 1
        posicoes["Dragão"][1] += 2
    print(simulaJogo(posicoes))
