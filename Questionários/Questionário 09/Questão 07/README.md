Vini é um menino muito travesso e gosta de brincar com matrizes. Um dia Vini pensou em representar uma tela do computador como uma matriz de dimensões \20\) linhas por 40 colunas. Se todas as posições desta matriz tivessem como valor um espaço em branco, esta matriz seria uma tela em branco.

Neste momento Vini pensou em representar nesta matriz a função matemático cocseno(x). Mas ele queria que a cossenóide desenhada na sua matriz tivesse um ciclo completo e ficasse no meio da tela. Também queria que a cossenóide não ficasse achatada. Por isso criou uma função para desenhar no espaço 2D a sua cossenóide, tendo como parâmetros o deslocamento da função cossenóide para que ela ficasse no meio da tela e a amplitude para que a cossenóide não ficasse achatada. Como a maior parte da matriz resultante era de espaços em branco, Vini representou esta matriz como uma matriz esparsa usando um dicionário. Corrija a função implementada por Vini para desenhar a cossenóide na tela.

```.py
import math

def TwoDSpace(deslocamento, amplitude, espaço):
    dicionario ={}
    for i in range(40):
            j = int(deslocamento - amplitude*math.cos(10*i*math.pi/180))
            dicionario[(i, j)] = "*"
    for j in range(20):
        for i in range(40):
            print(dicionario[i,j])
```
