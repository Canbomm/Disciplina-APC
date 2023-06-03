# zoninha que eu sei pra testar e criar a função que printa os horários

lista = ['2M1 CIC0004B', '2M2 CIC0004B', '2M3 IQD01263', '2M4 IQD01263', '2T2 MAT0025R', '2T3 MAT0025R', '3M1 CIC0004B', 
'3M2 CIC0004B', '3M3 IQD0125F', '3M4 IQD0125F', '3T2 IFD0171J', '3T3 IFD0171J', '4M3 IFD0173A', '4M4 IFD0173A',
'4T2 MAT0025R', '4T3 MAT0025R', '5M1 CIC0004B', '5M2 CIC0004B', '5M3 IQD0125F', '5M4 IQD0125F', '5T2 IFD0171J', 
'5T3 IFD0171J', '6M1 ENM0133A', '6M2 ENM0133A', '6T2 MAT0025R', '6T3 MAT0025R']

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

dic_espacos = {2:18,3:29,4:40,5:51,6:62,7:73}

def interpretaTurnos(lista):
    turnos = []
    for elem in lista:
        elementos = elem.split()
        horario = elementos[0]
        turnos.append(horario[1:])
    return list(dict.fromkeys(turnos))

def printaGrade(lista,dic_horarios):
    divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
    cabecalho = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    g_horaria = [divisao,cabecalho,divisao]
    if len(lista) != 0:
        for e in lista:
            e = e.split()
            horario = e[0]
            turno = [dic_horarios[horario[1:]]]
            for h in g_horaria:
                if not h == divisao and not h == cabecalho:
                    if (turno[0][2:15]) == (h[2:15]):
                        dia_semana = horario[0]
                        print("Oi")
                        #espacos = dia_semana - 2
                        #["| ",turno[0][2:15]," |",
            g_horaria += turno

def printaGrade2(lista,dic_horarios):
    # elementos base
    divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
    cabecalho = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    g_horaria = [divisao,cabecalho,divisao]
    # elementos interpretados
    if not len(lista) == 0:
        turnos = interpretaTurnos(lista)
        for elem in turnos:
            g_horaria.append(dic_horarios[elem])
            g_horaria.append(divisao)
        i = len(lista)-1
        while i >= 0:
            horarios = lista[i].split()
            # 2T2
            horario = horarios[0]
            # CIC0004F
            codigo = horarios[1]
            for linha in g_horaria:
                if not linha == divisao and not linha == cabecalho:
                    print(turnos)
                    print(horario)
                    turno = dic_horarios[horario[1:]][2:15]
                    print(f"{turno}")
                    break
            break
            i -= 1

def printaGrade2(lista,horarios,espacos):
    # elementos base
    divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
    cabecalho = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    g_horaria = [divisao,cabecalho,divisao]
    # elementos interpretados
    if not len(lista) == 0:
        i = len(lista)-1
        # mudando a linha
        while i >= 0:
            interpreta = lista[i].split()
            # 2T2
            horario = interpreta[0]
            # CIC0004F
            codigo = interpreta[1]
            # | 14:55 - 15:50 |          |          |          |          |          |          |
            linha = horarios[horario[1:]]
            pula = espacos[int(horario[0])]
            nova_linha = linha[0:pula] + codigo + linha[pula+8:]
            horarios[horario[1:]] = nova_linha
            i -= 1
    turnos = interpretaTurnos(lista)
    print(turnos)
    for elem in turnos:
        g_horaria.append(horarios[elem])
        g_horaria.append(divisao)
    for linha in g_horaria:
        print(linha)

lista2 = ['2T2 CIC0004F', '2T3 CIC0004F', '4T2 CIC0004F', '4T3 CIC0004F', '6T2 CIC0004F', '6T3 CIC0004F']

lista3 = []

lista4 = ['2M5 CIC0116L', '2T1 CIC0116L', '4M5 CIC0116L', '4T1 CIC0116L', '7N1 CIC0136E', '7N2 CIC0136E', '7N3 CIC0136E', '7N4 CIC0136E']

printaGrade2(lista4,dic_horarios,dic_espacos)
