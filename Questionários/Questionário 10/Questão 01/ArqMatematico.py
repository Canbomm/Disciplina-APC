nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha)
    for i in range(0,len(lido)-1):
        lido[i] = lido[i][:-1]

operacao = lido[1]
num1 = int(lido[0])
num2 = int(lido[2])

resultado = eval(f"{num1} {operacao} {num2}")
print(int(resultado))
