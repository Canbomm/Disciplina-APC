def calcula_f(a,b,c,x):
    return ((a*x**2)+(b*x)+c)

def calcula_delta(a,b,c,x):
    delta = (b*b - 4*a*c)
    if delta < 0:
        return "Equacao sem raizes reais"
    else:
        print(f"O resultado de f({x}) eh:", calcula_f(a,b,c,x), end=" ")
        return ""

print(calcula_delta(4,0,-16,1))