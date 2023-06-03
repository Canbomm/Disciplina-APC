import math

def TwoDSpace(deslocamento, amplitude, espaço):
    dicionario ={}
    for i in range(40):
            j = int(deslocamento - amplitude*math.cos(10*i*math.pi/180))
            dicionario[(i, j)] = "*"
    for j in range(20):
        for i in range(40):
            try:
                print(dicionario[(i,j)],end="")
            except:
                print(espaço,end="")
        print()

# TwoDSpace(10, 8, ".")