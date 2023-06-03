menor = float("inf")

while True:
    nome,salario = input().split(",")
    salario = float(salario)
    if nome == "Fim":
        break

    if salario < menor:
        recebe_menos = nome
        menor = salario

if menor == float("inf"):
    print("Não tem")
else:
    print(recebe_menos)
