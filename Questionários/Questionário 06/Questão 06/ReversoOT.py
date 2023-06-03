# obrigado monitor por me ensinar a fazer dessa forma
n = int(input("Digite qualquer número\n"))

# verificando se um número é negativo, e transformando em positivo
negativo = False
if n < 0:
    n = abs(n)
    negativo = True

# invertendo usando o método de string
inverso = int(str(n)[::-1])

# voltando o numero pra negativo
if negativo == True:
    inverso *= (-1)

print(f"Seu número invertido é {inverso}")
