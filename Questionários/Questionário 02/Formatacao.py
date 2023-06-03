num1 = int(input())
num2 = int(input())
formatacao = int(input())

operacao = num1/num2

print(f"O resultado de {num1} por {num2} é {operacao:.{formatacao}f}.")
