# essa versão possuía um validador muito "especifico" e está incompleta
def Validador(texto):
    # primeiro termo é um + ou -
    if not (texto[0] == "+" or texto[0] == "-"):
        return False
    # verifica se o segundo termo e um espaco
    if not texto[1] == " ":
        return False
    # verifica se os 3 primeiros termos são letras
    for i in range(2,5):
        e = texto[i]
        e = ord(e)
        if not (e >= 65 and e <= 90):
            return False
    # verifica se o codigo está composto por números
    for i in range(5,9):
        e = texto[i]
        e = ord(e)
        if not (e >= 48 and e <= 57):
            return False
    # verifica a turma
    if not (ord(texto[9]) >= 65 and ord(texto[9]) <= 90):
        return False
    if not texto[10] == " ":
        return False
    # validar horarios
    v_horarios = texto.split()
    for v in v_horarios[2:]:
        for c in v:
            c = ord(c)
            if c >= 65 and c <= 90:
                c = chr(c)
                if not (c == "M" or c == "T" or c == "N"):
                    return False
    return True

def PegaHorario(texto):
    # transforma os horarios em uma lista
    texto = texto[11:].split()
    grade_horaria = []
    for horario in texto:
        # index da letra
        for l in horario:
            if l == "M" or l == "T" or l == "N":
                h_dia_semana = l
        # h_ind_t = index do horário que contém o turno.
        h_ind_t = horario.find(h_dia_semana)
        # pegando os dias da semana e os horarios
        h_dias_semana = horario[:h_ind_t]
        h_tempos = horario[h_ind_t+1:]
        # transformando horários maiores em vários pequenos
        if len(h_dias_semana) == 1:
            if len(h_tempos) == 1:
                grade_horaria.append(h_dias_semana + h_dia_semana + h_tempos)
            else:
                for t in h_tempos:
                    grade_horaria.append(h_dias_semana + h_dia_semana + t)
        else:
            if len(h_tempos) == 1:
                for d in h_dias_semana:
                    grade_horaria.append(d + h_dia_semana + h_tempos)
            else:
                for d in h_dias_semana:
                    for t in h_tempos:
                        grade_horaria.append(d + h_dia_semana + t)
    return grade_horaria

def TemNaLista(lista,horario_n,codigo):
    """jatem = True, True -> Mesmo horario, mesmo codigo
    jatem = True, False -> Mesmo horario, codigo diferente
    jatem = False, False -> Horario diferente, codigo diferente"""
    for i in lista:
        # horario atual
        horario_a = i.split()
        # [codigo, horario]
        if horario_a[0] == codigo[0:8]:
            if horario_a[1] == horario_n:
                return True, True
        else:
            if horario_a[1] == horario_n:
                return True, False
    return False, False

def PrintaHorario(grade):
    # cabecalho
    g_divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
    g_espacamento_interno = " "*10
    g_cabecalho = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    cabecalho = [g_divisao,g_cabecalho,g_divisao]

g_horarios = []
# fazendo o loop
while True:
    # input
    g_horarios_temp = []
    inputs = input()
    # criterio de parada
    if inputs == "tchau":
        break
    # mostrador de grade
    if inputs == "?":
        # PARTE FINAL, A PARTE QUE FALTA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(g_horarios)
        #PrintaHorario(g_horarios)
    # coracao do codigo, essa parte que faz toda a validacao do input e trata ele
    else:
        if not Validador(inputs):
            print(f"!({inputs})")
        else:
            codigo = inputs[2:11]
            if inputs[0] == "+":
                horarios = PegaHorario(inputs)
                for h in horarios:
                    jatem = TemNaLista(g_horarios,h,codigo)
                    # verificando se pode adicionar
                    if not jatem[0] and not jatem[1]:
                        g_horarios_temp.append(codigo+h)
                    else:
                        print(f"!({inputs})")
                        g_horarios_temp = []
                        break
                g_horarios += g_horarios_temp
            elif inputs[0] == "-":
                horarios = PegaHorario(inputs)
                for h in horarios:
                    jatem = TemNaLista(g_horarios,h,codigo)
                    # verificando se pode remover
                    if jatem[0] and jatem[1]:
                        g_horarios_temp.append(codigo+h)
                    else:
                        print(f"!({inputs})")
                        g_horarios_temp = []
                        break
                for h in g_horarios_temp:
                    g_horarios.remove(h)
            else:
                print(f"!({inputs})")
