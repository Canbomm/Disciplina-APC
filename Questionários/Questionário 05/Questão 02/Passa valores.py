def repassaValores(a,b):
    print("Aqui é a função de repassar! Estou repassando a e b!")
    resultado = calculaValores(a,b)
    print(resultado)

def calculaValores(a,b):
    print("Sou a função de calcular. Calculando...")
    print("Tenho o resultado! Retornando!")
    return a+b

a = int(input())
b = int(input())
repassaValores(a,b)
