def corrida(posJ,posG):
    # a multiplicacao tem que acontecer primeiro, pois ele so quer a posicao de descanco
    novoposJ = posJ*3
    novoposG = posG*2
    if novoposJ > novoposG:
        print("Jorge ultrapassou e nao sera alcancado!")
    else:
        print(f"J: {novoposJ} G: {novoposG}")
        corrida(novoposJ,novoposG)
