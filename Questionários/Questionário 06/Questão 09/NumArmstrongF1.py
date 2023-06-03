# Tentativa falha, esse código não funciona

n = int(input())

def inverte(a):
    if a == 0:
        return 0
    else:
        # pegando a ultima casa e botando na primeira posição
        qcasas = len(str(a))
        ultimac = a%10
        invertido = ultimac * (10**(qcasas-1))
        # tratar o número pra poder adicionar a recursividade
        tratado = int((a-ultimac)/10)
        resultado = inverte(tratado)
        # somar o valor pra obter apenas um resultado
        resultado += invertido
        return resultado

numtratado = str(inverte(n))
ordem = len(str(n))
numtratado = " ".join(numtratado)
numtratado = numtratado.split(" ")
soma = 0
""" for numero in numtratado:
    print(f"+ {numero}^{ordem}", end=" ")
    numero = int(numero)
    print(f"+ {numero**ordem}", end=" ")
    soma += numero**ordem """
print(numtratado)