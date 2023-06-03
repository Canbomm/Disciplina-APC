nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha.rstrip())

cabecalho = lido[0].split(",")
Qfornecedores, Qitens = cabecalho[0].split()
fornecedores = cabecalho[1:]

for i in range(1,int(Qitens)+1):
    linha = lido[i].split(",")
    item = linha.pop(0)

    menor = float('inf')
    for i in range(0,len(linha)):
        if float(linha[i]) < menor:
            menor = float(linha[i])
            fornecedor = fornecedores[i]
    print(f"{item} {fornecedor}")
