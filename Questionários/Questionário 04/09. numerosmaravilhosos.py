def maravilhosos(num):
    num = int(num)
    if num <= 1:
        print(1)
    elif num % 2 == 0:
        print(num)
        maravilhosos(num/2)
    else:
        print(num)
        maravilhosos(3*num+1)

valor = int(input())
maravilhosos(valor)
