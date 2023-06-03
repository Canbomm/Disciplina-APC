def pattern(n):
    print(n)
    if n > 0:
        pattern(n-5)
        print(n)
    else:
        return n+5
# Eu realmente não sei como que isso daqui da certo, o return só acontece uma vez mas ele vai incrementando de alguma forma

# Testando valores
# pattern(10)
