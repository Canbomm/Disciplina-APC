def print_rectangle(x):
    tag = "+"
    espaco = " "
    print(x)
    print(x*tag)
    print(f"{tag}{(x-2)*espaco}{tag}")
    print(x*tag)

piscina1,piscina2,piscina3 = map(int,input().split())
print_rectangle(piscina1)
print_rectangle(piscina2)
print_rectangle(piscina3)
