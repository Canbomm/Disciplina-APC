from cmath import inf

# não usei essa variável para nada
quantmeias = int(input())

meias = [int(x) for x in input().split()]
meias.append(float(inf))
meias.sort()

for i in range(0,len(meias),2):
    if meias[i] != meias[i+1]:
        print(f"{meias[i]} sozinho")
        break
