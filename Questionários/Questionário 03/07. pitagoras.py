#Realize as alterações necessárias no código apresentado.
def pitagoras(b, c):
    a = (b*b + c*c)**0.5
    a = int(a)
    print(a)

b, c = map(float,input().split())
pitagoras(b, c)
