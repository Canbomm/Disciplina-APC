def soma_harmonica(x):
    if x == 1:
        return 1
    elif x > 1:
        return (1/x) + soma_harmonica(x-1)
    else:
        return 0

# testando valores
# print(soma_harmonica(0))