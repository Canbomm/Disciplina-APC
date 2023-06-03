def feedback(nota):
    if nota == 40:
        print("Lendaaaaario!", end="")
    elif 36 <= nota <= 39:
        print(f"Excelente!!!! Saldo: +{nota - 28}", end="")
    elif 29 <= nota <= 35:
        print(f"Mandou bem! Continue estudando que voce vai fechar a prova ;) Saldo: +{nota - 28}", end="")
    elif nota == 28:
        print(f"Mandou bem! Continue estudando que voce vai fechar a prova ;)", end="")
    elif 26 <= nota <= 27:
        print(f"Foi quaaaaaaase, vamos estudar mais pra passar semana que vem (: Saldo: -{28 - nota}", end="")
    else:
        print(f"Car@ alun@, revise a materia toda! Nao foi dessa vez, mas nao desista! Rumo aos 28!!! Saldo: -{28 - nota}", end="")
    return ""

# Testando valores
# print(feedback(26))
