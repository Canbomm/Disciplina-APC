entrada = input()
meio = len(entrada)//2
comeco = entrada[:meio]
final = entrada[meio:][::-1]

# comparando
dif = 0
for ind in range(0,len(comeco)):
    if comeco[ind] != final[ind]:
        dif += 1

if len(entrada) % 2 == 1:
    if dif > 1:
        print("OFF")
    else:
        print("ON")
else:
    if dif == 1:
        print("ON")
    else:
        print("OFF")
