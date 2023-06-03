frase = input()
comeco,fim = map(int,input().split())

print(f"{frase[(comeco-1):fim]}")
