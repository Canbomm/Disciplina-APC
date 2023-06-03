ate_numero = int(input())
num_teste = 0

print("0",end=" ")

while num_teste < ate_numero:
    num_teste += 1
    # testando divisao por 3 e 7
    if num_teste % 3 == 0 and num_teste % 7 == 0:
        print(num_teste,end=" ")

print()
