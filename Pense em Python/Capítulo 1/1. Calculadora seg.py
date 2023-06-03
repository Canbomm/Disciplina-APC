print("Bem vindo a conversora automática de minutos, para responder a pergunta em seguida desconsidere os segundos")
min = int(input("Quantos minutos você deseja converter?\n"))
seg = int(input("Quantos segundos a mais você deseja adicionar?\n"))
#problema conhecido: Caso alguém coloque um valor não numérico a calculadora dá erro.
Tseg = min * 60 + seg

print(f"O valor total em segundos é",Tseg)
