print("Bem vindo a conversora de Km para milhas")
km = int(input("Quantas km você deseja converter?\n"))
#problema conhecido: Caso alguém coloque um valor não numérico a calculadora dá erro.
milhas = km / 1.61

print(km,f"km em milhas é {milhas:.2f}")
