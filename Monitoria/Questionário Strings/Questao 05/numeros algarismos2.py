entrada = input()
algarismos = {"zero":"0","um":"1","dois":"2","três":"3","quatro":"4","cinco":"5","seis":"6","sete":"7","oito":"8","nove":"9"}
for chave in algarismos:
    encontrou = entrada.find(chave)
    if encontrou != -1:
        entrada = entrada[:encontrou] + algarismos[chave] + entrada[encontrou+len(chave):]
print(entrada)
