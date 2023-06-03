frase = input()

histograma = {}
for carac in frase:
    if histograma.get(carac) != None:
        histograma[carac] += 1
    else:
        histograma[carac] = 1

print(histograma)

invHistograma = {}
for chave in histograma:
    if invHistograma.get(histograma[chave]) != None:
        invHistograma[histograma[chave]] += [chave]
    else:
        invHistograma[histograma[chave]] = [chave]

print(invHistograma)
