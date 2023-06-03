print("Bem vindo a calculadora de passos")
km = int(input("Quantos quilômetros você percorreu?\n"))
min = int(input("Quantos minutos você demorou?\n"))
seg = int(input("E quantos segundos?\n"))

tempoh = seg/3600 + min/60
milhas = km/1.61
ritmo = milhas/tempoh

print(f"Sua velocidade média é de {ritmo:.2f}")
