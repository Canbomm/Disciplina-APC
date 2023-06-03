# 3° tentativa, esse código sim funciona para números inteiros positivos

numero = int(input())
ordem = len(str(numero))
etapa1 = ""
etapa2 = ""
# vamos considerar o caso de 153

# inverte o numero (apenas positivos)
def inverte(a):
    a = str(a)[::-1]
    return a

# pega as casas decimais e separa em uma lista
lista = [str(x) for x in str(inverte(numero))]
# retornaria ["3","5","1"]

# verifica se é verdadeiro ou falso
resultado = 0
valores = [int(x) for x in lista]
# sequencia de Armstrong
for x in valores:
    resultado += x**ordem

# verifica se é verdadeiro
if resultado == numero:
    fim = f" = {numero}"
else:
    fim = f" != {numero}"

# printa a primeira etapa: as das somas
for x in lista:
    etapa1 = etapa1 + (str(x) + f"^{ordem}") + " "
etapa1 = etapa1.split()
print(' + '.join(etapa1), end=' = ')

# printa a segunda etapa: resolveu os expoentes
for x in lista:
    etapa2 = etapa2 + (str(int(x)**ordem)) + " "
etapa2 = etapa2.split()
print("\n",' + '.join(etapa2), fim, sep="")

# conclusão
if resultado == numero:
    print(f"{numero} é um número de Armstrong de {ordem} ordem.")
else:
    print(f"{numero} não é um número de Armstrong de {ordem} ordem.")
