# organizando os dias da semana
dias_semana = "|               |"
semana = ["Dom","Seg","Ter","Qua","Qui","Sex","Sab"]
# centralizando o dia da semana (ou pelo menos tentando)
espacamento_dias = int((9-3)/2)
if espacamento_dias % 2 != 0:
    for dia_semana in semana:
        dias_semana += ((int(espacamento_dias/2)*" ") + dia_semana + ((int(espacamento_dias/2))+1*" ") + "|")
else:
    for dia_semana in semana:
        dias_semana += ((int(espacamento_dias/2)*" ") + dia_semana + (int(espacamento_dias/2)*" ") + "|")

print(dias_semana)
