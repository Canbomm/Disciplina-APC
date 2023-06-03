nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha.rstrip())

numero_magico = int(lido[0])
vetor = lido[1]
vetores = vetor.split()

def agrupaLista(lista,passo):
    nova_lista = []
    for i in range(0,len(lista)):
        conjunto = lista[i:i+passo]
        nova_lista.append(conjunto)
    return nova_lista

def bonitoPedro(lista,numero_magico):
    maior = int(max(lista))
    if (maior*2) > len(lista) and (2*numero_magico) <= maior:
        return True
    return False

def bonito2Pedro(lista,numero_magico):
    menor = int(min(lista))
    if menor <= ((len(lista))/2) and menor <= (numero_magico)/2:
        return True
    return False

listas = agrupaLista(vetores,numero_magico)
QbonitoPedro = 0
Qbonito2Pedro = 0

for lista in listas:
    if bonitoPedro(lista,numero_magico):
        QbonitoPedro += 1
    if bonito2Pedro(lista,numero_magico):
        Qbonito2Pedro += 1

print(QbonitoPedro,Qbonito2Pedro)
