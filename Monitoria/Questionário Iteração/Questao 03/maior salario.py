maior = 0

while True:
    nome,salario = input().split(",")
    salario = float(salario)
    if nome == "Fim":
        break

    if salario > maior:
        maior = salario

if maior == 0:
    print("Não tem")
else:
    print(f"{maior:.2f}")
