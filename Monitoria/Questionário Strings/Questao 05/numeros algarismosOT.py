entrada = input().split()
algarismos = {"um":"1","dois":"2","três":"3","quatro":"4","cinco":"5","seis":"6","sete":"7","oito":"8","nove":"9"}
saida = ""
for pal in entrada:
    if algarismos.get(pal) != None:
        saida += (algarismos.get(pal) + " ")
    else:
        saida += (pal + " ")
print(saida)
