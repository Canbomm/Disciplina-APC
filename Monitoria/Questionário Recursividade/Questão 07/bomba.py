tempo_inicial = int(input())
tempo_recorde = int(input())

def bomba(inicial,recorde,original):
    desativou = False
    # mensagens em relacao ao tempo
    if inicial == 5:
        print(f"Seu tempo está acabando!")
    elif inicial == 1:
        if recorde >= original:
            desativou = True
        else:
            print(f"Seja rápido. Falta 1 segundo")
    else:
        if inicial != 0:
            print(f"Atenção faltam {inicial} segundos...")
        
    novo_tempo = inicial - 1

    if novo_tempo > 0:
        bomba(novo_tempo,recorde,original)
    else:
        if desativou:
            print("Bomba desativada automaticamente!")
        else:
            print("Cabum!!!! Explodiu")

bomba(tempo_inicial,tempo_recorde,tempo_inicial)
