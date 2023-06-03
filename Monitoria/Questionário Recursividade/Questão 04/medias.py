num1,num2,num3 = [int(x) for x in input().split()]
# numeros = map(int, input().split())
operacao = input()

# P = ponderada
# H = harmonica
# A = aritmetica
if operacao == "P":
    print("Ponderada")
    peso1,peso2,peso3 = [int(x) for x in input().split()]
    media = ((peso1*num1)+(peso2*num2)+(peso3*num3))/(peso1+peso2+peso3)
    print(f"{media:.2f}")

elif operacao == "H":
    print("Harmonica")
    media = 3/(1/num1 + 1/num2 + 1/num3)
    print(f"{media:.2f}")

elif operacao == "A":
    print("Aritmetica")
    media = (num1+num2+num3)/3
    print(f"{media:.2f}")
    
else:
    print("Operacao inexistente")
