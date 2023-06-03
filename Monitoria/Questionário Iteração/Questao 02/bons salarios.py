salario_total = 0
empregados = 0

while True:
    nome,salario = input().split(",")
    if nome == "Fim":
        break
    salario_total += float(salario)
    empregados += 1

if empregados <= 0:
    print("0.00")
else:
    print(f"{salario_total/empregados:.2f}")
    