def interpretaAPC(lista):
    resp = 0
    conta = -1
    for e in lista:
        resp += (e * 2**(conta))
        conta -= 1
    return resp

got      = [0, 0, 1, 1, 1, 1]
expected = [1, 0, 0, 1, 1, 1]

print(f"Oq eu fiz: {interpretaAPC(got)}\nOq eles querem: {interpretaAPC(expected)}")
