def imprimeTermos(num):
    if num <= 0:
        print("0")
    else:
        print(num)
        imprimeTermos(num-2)
