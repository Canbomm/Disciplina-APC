entradas = input().split()
n1 = int(entradas[0])
n2 = int(entradas[1])
n3 = int(entradas[2])

def media(nota,prova):
    if nota >= 5 and nota < 7:
        print(f'{prova}: MM')
    elif nota >= 7 and nota < 9:
        print(f'{prova}: MS')
    else:
        print(f'{prova}: SS')

if n1 >= 5 and n2 >= 5 and n3 >= 5:
    print('APROVAR')
    media(n1,"Prova1")
    media(n2,"Prova2")
    media(n3,"Prova3")
        
else:
    print('REPROVAR')
