lista = []
for _ in range(0,int(input())):
    nome = input()
    lista.append(nome)

for nome in lista[::-1]:
    print(nome)
