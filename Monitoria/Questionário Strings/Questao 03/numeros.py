entrada = input()
digitos = 0
for char in entrada:
    if char.isnumeric():
        digitos += 1
print(digitos)
