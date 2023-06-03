entrada = input()
saida = ""
for char in entrada[1::2]:
    if char != " ":
        saida += char
print(saida)
