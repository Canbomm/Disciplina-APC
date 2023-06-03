banda,bandasrockinrio = input().split()

# caso ele nao encontre em nenhum lugar da string ele vai retornar -1
temapresentacao = bandasrockinrio.find(banda)

if temapresentacao == -1:
    print(f"por que o jimin nao vai vir pro brasil? ;-;")
else:
    print(f"A banda {banda} ira se apresentar na RIR!")
