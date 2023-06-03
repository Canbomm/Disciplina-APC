repeticao = 5
verso = {}

while repeticao > 0:
    repeticao -=1
    chave = input()
    valor = int(input())
    verso[chave] = valor

print(verso)

# hora de reverter o dicionário
reverso = {}
chaves = list(verso.keys())
index = 0

while index < 5:
    reverso[verso[chaves[index]]] = chaves[index]
    index += 1

print(reverso)
