# Tentativa 1, deu errado
n = int(input())

if n >= 0:
    # positivo
    n = str(n)
    print(f"{n[::-1]}")
else:
    n = (n**2)**(1/2)
    n = int(n)
    n = str(n)
    print(f"-{n[::-1]}")

# Tentativa 2, deu errado também
n = input()

if n.count("-") == 0:
    # positivo
    print(f"{n[::-1]}")
else:
    print(f"-{n[:0:-1]}")

# Não consegui pontuação máxima, provavelmente por trabalhar com str, o caso -20 por exemplo, deveria retornar -2, mas retorna -02