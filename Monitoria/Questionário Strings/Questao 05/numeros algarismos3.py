entrada = input().split(":")
saida = "".join(entrada[:-1])
mudar = entrada[-1]

# tentando dar replace
algarismos = "zero um dois três quatro cinco seis sete oito nove".split(" ")
indice = 0
for algarism in algarismos:
    mudar = mudar.replace(algarism,str(indice))
    indice += 1
print(f"{saida + ':' + mudar}")
