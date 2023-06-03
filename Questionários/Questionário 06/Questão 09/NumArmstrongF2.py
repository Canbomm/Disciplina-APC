# Tentativa falha, esse código não funciona

n = int(input())
ordem = len(str(n))
# quantidade de sinais

def Armstrong(a):
    if a == 0:
        return
    else:
        ultimac = a%10
        proximo = ((a-ultimac)/10)
        print(etapas(ultimac))
        Armstrong(int(proximo))

def etapas(b):
    qdesinais = (len(str(b))-1)
    if qdesinais > 0:
        frase += f"{b}^{ordem}" + "+"
    else:
        frase += f"{b}^{ordem} ="

Armstrong(n)