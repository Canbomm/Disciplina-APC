menor = float("inf")
maior = 0
salario_total = 0
total_empregados = int(input())
parada = 0

while parada < total_empregados:
    nome,salario = input().split(",")
    salario = float(salario)
    
    # determinando o menor salario e o nome
    if salario < menor:
        recebe_menos = nome
        menor = salario
    
    # determinando o maior salario e o nome
    if salario > maior:
        recebe_mais = nome
        maior = salario
    
    # pegando os salarios para fazer a media
    salario_total += salario
    parada += 1

# printando os resultados
if total_empregados == 0:
    print("Não tem média")
    print("Não tem")
    print("Não tem")
else:
    print(f"{salario_total/total_empregados:.2f}")
    print(f"{recebe_mais} {maior:.2f}")
    print(f"{recebe_menos} {menor:.2f}")
