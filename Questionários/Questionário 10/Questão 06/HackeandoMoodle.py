with open("/etc/passwd") as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha.rstrip())

linha = int(input())
print((lido[linha-1].split(":"))[0])
