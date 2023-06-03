# minuto inical e final
minicial,mfinal = map(int,input().split())
numeros = ""

for i in range(minicial,mfinal+1):
    # pegando os tempos em que ovnis aparecem
    if (i**(1/2))%1 == 0:
        valor = str(i)
        numeros += valor + " "
numeros = numeros[:-1].split()
tempos = [int(i) for i in numeros]
if len(tempos) <= 1:
    print(0)
else:
    penultimot = int(numeros[-2])
    ultimot = int(numeros[-1])

    maiort = ultimot - (penultimot + 1)
    print(maiort)
# resolvi isso sem entender muito de lista, mas graças ao google eu sabia o que eu precisava
