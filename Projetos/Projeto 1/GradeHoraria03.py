def VerificadorInput(lista):
    """Verifica se o input está escrito corretamente, retorna Falso caso contrário"""
    # verifica se tem um mais ou menos
    if not (lista[0] == "+" or lista[0] == "-"):
        return False
    # verifica se o código tem um tamanho correto
    elif len(lista[1]) != 8:
        return False
    # verifica os horários
    else:
        horarios = lista[2:]
        for horario in horarios:
            letras = AchaLetra(horario)
            # verifica se o turno está correto
            if not (letras[0] == "M" or letras[0] == "T" or letras[0] == "N"):
                return False
            # verifica se o dia da semana nao "estourou"
            for n in horario[:(letras[1])]:
                if int(n) > 7 or int(n) < 2:
                    return False
            # verifica se o horario nao "estourou"
            for n in horario[(letras[1])+1:]:
                if letras[0] == "N":
                    if int(n) > 4:
                        return False
                else:
                    if int(n) > 5:
                        return False
    return True

def VerificadorHorario(lista):
    turnos = []
    # pega cada horario e considera apenas o turno
    for h in lista:
        h = h.split()
        turnos.append(h[0])
    # confere se tem horarios iguais
    for t in turnos:
        if turnos.count(t) != 1:
            return False
    return True

def AchaLetra(string):
    for c in string:
        if not c.isnumeric():
            letra = c
            letra_index = string.index(c)
    return letra,letra_index

def pegaHorarios(lista,codigo):
    tratados = []
    for h in lista:
        if len(h) == 3:
            tratados.append(h + " " + codigo)
        else:
            letra = AchaLetra(h)
            dias_semana = h[0:letra[1]]
            horarios = h[letra[1]+1:]
            for cd in dias_semana:
                for ch in horarios:
                    horario = cd + letra[0] + ch + " " + codigo
                    tratados.append(horario)
    return tratados

def removeHorarios(lista,listaremove):
    listaoriginal = []
    for e in lista:
        listaoriginal.append(e)
    if len(lista) == 0:
        return ["Erro"]
    else:
        listona = lista + listaremove
        for e in listona:
            if listona.count(e) != 1:
                lista.pop(lista.index(e))
                listona = lista + listaremove
    if listaoriginal == lista:
        return ["Erro"]
    else:
        return lista

def interpretaTurnos(lista):
    turnos = []
    for elem in lista:
        elementos = elem.split()
        horario = elementos[0]
        turnos.append(horario[1:])
    return list(dict.fromkeys(turnos))

def printaGrade(lista):
    # dicionário com todos os horários utilizados
    dic_horarios = {
    "M1":"| 08:00 - 08:55 |          |          |          |          |          |          |",
    "M2":"| 08:55 - 09:50 |          |          |          |          |          |          |",
    "M3":"| 10:00 - 10:55 |          |          |          |          |          |          |",
    "M4":"| 10:55 - 11:50 |          |          |          |          |          |          |",
    "M5":"| 12:00 - 12:55 |          |          |          |          |          |          |",
    "T1":"| 12:55 - 13:50 |          |          |          |          |          |          |",
    "T2":"| 14:00 - 14:55 |          |          |          |          |          |          |",
    "T3":"| 14:55 - 15:50 |          |          |          |          |          |          |",
    "T4":"| 16:00 - 16:55 |          |          |          |          |          |          |",
    "T5":"| 16:55 - 17:50 |          |          |          |          |          |          |",
    "N1":"| 19:00 - 19:50 |          |          |          |          |          |          |",
    "N2":"| 19:50 - 20:40 |          |          |          |          |          |          |",
    "N3":"| 20:50 - 21:40 |          |          |          |          |          |          |",
    "N4":"| 21:40 - 22:30 |          |          |          |          |          |          |"
    }
    # dicionário com o número de espaços que tem antes de onde coloca o código
    dic_espacos = {2:18,3:29,4:40,5:51,6:62,7:73}
    # elementos base
    divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
    cabecalho = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    g_horaria = [divisao,cabecalho,divisao]
    # elementos interpretados
    if not len(lista) == 0:
        i = len(lista)-1
        # mudando a linha
        while i >= 0:
            horarios = lista[i].split()
            # 2T2
            horario = horarios[0]
            # CIC0004F
            codigo = horarios[1]
            # | 14:55 - 15:50 |          |          |          |          |          |          |
            linha = dic_horarios[horario[1:]]
            pula = dic_espacos[int(horario[0])]
            nova_linha = linha[0:pula] + codigo + linha[pula+8:]
            dic_horarios[horario[1:]] = nova_linha
            i -= 1
    turnos = interpretaTurnos(lista)
    for elem in turnos:
        g_horaria.append(dic_horarios[elem])
        g_horaria.append(divisao)
    for linha in g_horaria:
        print(linha)

def organizadora(lista):
    SORT_ORDER = {"M":0,"T":1,"N":2}
    turnos = []
    organizada = []
    for elem in lista:
        index = lista.index(elem)
        horario = elem.split()
        turno = horario[0][1]
        tupla = (turno,index)
        turnos.append(tupla)
    turnos = sorted(turnos, key=lambda val: SORT_ORDER[val[0]])
    for tupla in turnos:
        index = tupla[1]
        organizada.append(lista[index])
    return organizada

g_horaria = []
g_horaria_temp = []

while True:
    inputs = input()
    # termina o código
    if inputs == "Hasta la vista, beibe!":
        break
    elif inputs == "":
        print(f"!({inputs})")
    # imprime a grade atual
    elif inputs == "?":
        g_horaria.sort()
        g_horaria = organizadora(g_horaria)
        printaGrade(g_horaria)
    # trabalha com o input
    else:
        verifica = inputs.split()
        # verifica se o codigo esta escrito certo
        eValido = VerificadorInput(verifica)
        if not eValido:
            print(f"!({inputs})")
        else:
            horarios = pegaHorarios(verifica[2:],verifica[1])
            # verifica se os horarios dados possuem conflito entre si
            passou_h = VerificadorHorario(horarios)
            if passou_h:
                if verifica[0] == "+":
                    g_horaria_temp += horarios
                    passou_g = VerificadorHorario(g_horaria_temp)
                    # verifica se pode adicionar os horarios novos
                    if passou_g:
                        # g_horaria = g_horaria_temp
                        g_horaria = []
                        for e in g_horaria_temp:
                            g_horaria.append(e)
                    else:
                        g_horaria_temp = []
                        for e in g_horaria:
                            g_horaria_temp.append(e)
                        print(f"!({inputs})")
                else:
                    g_horaria_temp = removeHorarios(g_horaria_temp,horarios)
                    if g_horaria_temp == ["Erro"]:
                        # g_horaria_temp = g_horaria
                        g_horaria_temp = []
                        for e in g_horaria:
                            g_horaria_temp.append(e)
                        print(f"!({inputs})")
                    else:
                        # g_horaria = g_horaria_temp
                        g_horaria = []
                        for e in g_horaria_temp:
                            g_horaria.append(e)
            else:
                print(f"!({inputs})")
