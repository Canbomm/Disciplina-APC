def duplica(f):
    f()
    f()
    f()

def duplica_o_duplicado(f):
    duplica(f)
    duplica(f)
    
def imprime_parte_linha1():
    print(s1+s2, end="")
    
def imprime_parte_linha1_fim():
    print(s1)
    
def imprime_parte_linha2():
    print(s3+s4, end="")
    
def imprime_parte_linha2_fim():
    print(s3)
    
def imprime_linha1():
    duplica_o_duplicado(imprime_parte_linha1)
    imprime_parte_linha1_fim()

def imprime_linha2():
    duplica_o_duplicado(imprime_parte_linha2)
    imprime_parte_linha2_fim()
    
def imprime_parte_padrão():
    imprime_linha1()
    imprime_linha2()
          
def imprime_padrão():
    duplica_o_duplicado(imprime_parte_padrão)
    imprime_linha1()

s1, s2, s3, s4 = input().split()

imprime_padrão()
