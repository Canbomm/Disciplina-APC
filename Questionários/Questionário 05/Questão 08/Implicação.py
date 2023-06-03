def cond(p,q,r):
    if p == True and q == True:
        # p -> q = True
        if r == True:
            return True
        else:
            return False
    elif p == True and q == False:
        # p -> q = False
        # F -> V = True
        # F -> F = True
        # ou seja, sempre vai retornar True
        return True
    elif p == False and q == True:
        # p -> q = True
        if r == True:
            return True
        else:   
            return False
    else:
        # p -> q = True
        if r == True:
            return True
        else:
            return False

# Deve dar pra otimizar esse código, mas eu nem sei pra que alguem usaria ele
# Testando valores
# print(cond(1 < 2, 1 < 3, 1 < 5))