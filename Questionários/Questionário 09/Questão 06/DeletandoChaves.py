numeros = {}
chave = input()

while chave != "fim":
    valor = int(input())
    numeros[chave] = valor
    chave = input()

media = 0
for chave in numeros:
    media += numeros[chave]
print(media)

remover = input()
if numeros.get(remover) != None:
    media -= numeros.pop(remover)
    print(media)
else:
    print("Essa chave não existe no dicionário")
