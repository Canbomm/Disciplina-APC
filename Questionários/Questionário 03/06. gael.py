import math

def calcula_tratamento_numeros(x,y):
    print(f"{x} elevado a {y} eh {x**y:.2f}")
    print(f"{y} elevado a {x} eh {y**x:.2f}")
    print(f"O maior entre {x} e {y} eh {max(x,y)}")
    print(f"A parte inteira de {x} eh {int(x)}")
    print(f"A parte fracionaria de {x} eh {round(x):.2f}")
    print(f"A parte inteira de {y} eh {int(y)}")
    print(f"A parte fracionaria de {y} eh {round(y):.2f}")

def calcula_area_geometrica(x,y):
    print(f"O quadrado de lado {x} tem area de tamanho {x*x:.2f}")
    print(f"O quadrado de lado {y} tem area de tamanho {y*y:.2f}")
    print(f"O circulo de raio {x} tem area de tamanho {math.pi * x * x:.2f}")
    print(f"O circulo de raio {y} tem area de tamanho {math.pi * y * y:.2f}")

#essas linhas servem apenas para testar o código
x,y = map(float,input().split())
calcula_tratamento_numeros(x,y)
print()
calcula_area_geometrica(x,y)
