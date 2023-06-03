"""
O legal dessa versao do projeto, e que a grade e modular
voce pode colocar qualquer tamanho de horario que quiser
que ele vai tentar imprimir algo bonito (nem sempre da).
O ruim e que falha no caso de teste padrao do questionario kkkkk
(o que imprime a grade vazia)
"""

# funcao que mostra a grade horaria
def printa_grade(grade,espacamento):
    # definindo divisao
    divisao = "+---------------+" + (("-"*espacamento) + "+")*7

    # organizando os dias da semana
    dias_semana = "|               |"
    semana = ["Dom","Seg","Ter","Qua","Qui","Sex","Sab"]
    for dia_semana in semana:
        dias_semana += (" " + dia_semana + ((espacamento-4)*" ") + "|")
    
    # terminando cabecalho
    cabecalho = [divisao,dias_semana,divisao]

    # printando o cabecalho
    for linha in cabecalho:
        print(linha)
    
    # definindo uma grade
    espaco = " "*espacamento + "|"
    horarios = {
    "M1":{0:"| 08:00 - 08:55 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "M2":{0:"| 08:55 - 09:50 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "M3":{0:"| 10:00 - 10:55 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "M4":{0:"| 10:55 - 11:50 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "M5":{0:"| 12:00 - 12:55 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "T1":{0:"| 12:55 - 13:50 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "T2":{0:"| 14:00 - 14:55 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "T3":{0:"| 14:55 - 15:50 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "T4":{0:"| 16:00 - 16:55 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "T5":{0:"| 16:55 - 17:50 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "T6":{0:"| 18:00 - 18:55 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "N1":{0:"| 19:00 - 19:50 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "N2":{0:"| 19:50 - 20:40 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "N3":{0:"| 20:50 - 21:40 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco},
    "N4":{0:"| 21:40 - 22:30 |",1:espaco,2:espaco,3:espaco,4:espaco,5:espaco,6:espaco,7:espaco}
    }

    # colocando os valores necessarios
    for chave in grade:
        turno = chave[1:]
        codigo = grade[chave]

        # definindo os espacos que irao vir antes e depois do codigo
        tam_str = len(codigo)+1
        espacos = " "*(espacamento-tam_str)
        
        # modificando o horario
        horarios[turno][int(chave[0])] = " " + codigo + espacos + "|"
    
    # printando a grade
    for turno in horarios:
        mudou = verificaMudou(horarios[turno],espaco)
        if mudou:
            for i in range(0,8):
                print(horarios[turno][i],sep="",end="")
            print("\n",divisao,sep="")

# verifica se uma linha da grade realmente mudou
def verificaMudou(linha,espaco):
    espacos = 0
    for i in range(1,8):
        if linha[i] == espaco:
            espacos += 1
    if espacos >= 6:
        return False
    else:
        return True

# funcao que verifica se o input esta correto
def verificador(lista,dicionario,espacamento,limites):   
    # tratando os horarios pro modelo ideal: DTH. D = Dia, T = Turno, H = Horario
    horarios = pega_horario(lista[2:],limites)
    # caso o pega_horario encontre algo de errado ele retorna None
    if horarios == None:
        return False,None,espacamento
    
    # verificando se algum horario ja existe caso o usuario queira adicionar
    if lista[0] == "+":
        for horario in horarios:
            if dicionario.get(horario) != None:
                # se caiu aqui o usuario quer adicionar um horario que ja existe
                return False,None,espacamento

    # mudando o espacamento caso necessario, o +2 sao os espacos que vem antes e depois do nome da materia
    tamanho_mat = len(lista[1]) + 2
    if tamanho_mat > espacamento:
        espacamento = tamanho_mat
    
    # retornando True pois tudo foi um sucesso, horarios e espacamento
    return True,horarios,espacamento

# funcao que separa os horarios
def pega_horario(codigos,limites):
    # definindo uma lista para armazenar os horarios tratados
    tratados = []

    # fazendo um for para caso receba mais de um turno
    for horario in codigos:
        # Garantindo que tenha apenas uma letra por horario
        pos_letra = -1

        # encontrando a letra que representa o turno
        for index,caractere in enumerate(horario):
            if caractere == "M" or caractere == "T" or caractere == "N":
                if pos_letra == -1:
                    pos_letra = index
                    turno_atual = caractere
                else:
                    # se entrou aqui, e porque tem mais de uma letra portanto o input ta errado
                    return None
        # se entrar no prox if, e porque percorreu o for inteiro e nao encontrou um turno valido
        if pos_letra == -1:
            return None
        
        # montando os horarios do jeito ideal

        # dias_horarios e uma lista cujo primeiro elemento representa os dias da semana e o segundo os horarios
        dias_horarios = horario.split(turno_atual)
        # fazendo a juncao
        for dia in dias_horarios[0]:
            # verificando se o dia da semana esta correto
            if int(dia) > 7 or int(dia) < 1:
                return None
            for horario in dias_horarios[1]:
                # verificando se o horario nao passou dos limites
                limite = limites.get(turno_atual)
                if int(horario) > limite or int(horario) < 1:
                    return None
                tratados.append(dia + turno_atual + horario)
    # retornando horarios tratados, aqui tudo ocorreu com o esperado
    return tratados

# funcao que adiciona horario
def adiciona_horario(grade,horarios,materia):
    for horario in horarios:
        grade[horario] = materia
    return grade

# funcao que remove horario
def remove_horario(grade,horarios,materia):
    # salvando caso aconteca alguma coisa
    grade_inical = grade

    # removendo os horarios
    for horario in horarios:
        # conferindo se a materia esta correta
        if grade.get(horario) == materia:
            grade.pop(horario)
        else:
            return False,grade_inical
    return True, grade

# definindo variaveis iniciais
grade = {}
espacamento = 4
limites_turnos = {"M":5,"T":6,"N":4}

# loop que le input
while True:
    # pegando input
    entrada = input()
    processada = entrada.split(" ")

    # printando a grade
    if processada[0] == "?":
        # mostra grade horaria
        printa_grade(grade,espacamento)
    
    # adicionando ou removendo horarios
    elif processada[0] == "+":
        # adiciona horario
        verificacao = verificador(processada,grade,espacamento,limites_turnos)
        espacamento = verificacao[2]
        if verificacao[0]:
            grade = adiciona_horario(grade,verificacao[1],processada[1])
        else:
            print(f"!({entrada})")
    elif processada[0] == "-":
        # remove horario
        verificacao = verificador(processada,grade,espacamento,limites_turnos)
        espacamento = verificacao[2]
        if verificacao[0]:
            # removeu e uma lista com 2 itens, caso o primeiro de False, o nome da materia esta errado
            # o segundo item do removeu e so a grade mesmo
            removeu = remove_horario(grade,verificacao[1],processada[1])
            if not removeu[0]:
                print(f"!({entrada})")
            else:
                grade = removeu[1]
        else:
            print(f"!({entrada})")
    
    # encerrando loop
    else:
        break
