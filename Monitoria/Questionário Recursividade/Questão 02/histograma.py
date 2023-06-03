entrada1 = input("O programa funciona?\n")

if entrada1 == "SIM":
    entrada2 = input("Você entende o que fez?\n")

    if entrada2 == "SIM":
        print("Ótimo. Então não mexe!")
    else:
        entrada3 = input("Já foi na tutoria?\n")

        if entrada3 == "SIM":
            print("Choremos!")
        else:
            print("Temos um time a disposição!")
else:
    entrada2 = input("Você sabe onde está o erro?\n")

    if entrada2 == "SIM":
        entrada3 = input("Acha que pode solucionar sozinho?\n")

        if entrada3 == "SIM":
            print("Então mão na massa!")
        else:
            entrada4 = input("Já pesquisou no Google?\n")

            if entrada4 == "SIM":
                entrada5 = input("Já foi na tutoria?\n")

                if entrada5 == "SIM":
                    print("Choremos!")
                else:
                    print("Temos um time a disposição!")
            else:
                print("Corre lá então!")
    else:
        entrada3 = input("Já foi na tutoria?\n")

        if entrada3 == "SIM":
            print("Choremos!")
        else:
            print("Temos um time a disposição!")
