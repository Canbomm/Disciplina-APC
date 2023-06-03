# lap = laptops
# ipa = ipads
# dia = dia do pagamento
# pag = metodo de pagamento
#     0 -> a vista
#     1 -> a prazo
# dis = distancia para entrega

lap, ipa, dia, pag, dis = input().split()
lap = int(lap)
ipa = int(ipa)
dia = int(dia)
pag = int(pag)
dis = int(dis)

valor = lap * 1500 + ipa * 1000;

if (lap + ipa) >= 3:
    valor = valor - 500
    
if pag == 0:
    if dia >= 16:
        valor = valor * 0.95
    else:
        valor = valor * 0.90
else:
    if dia <= 15:
        valor = valor * 1.08
    else:
        valor = valor * 1.10

if dis <= 50:
    valor = valor + 100
else:
    valor = valor + 200

print(f'{valor:.2f}')

# fiquei meia hora tentando achar o que tava dando errado, e ele tinha deixado o "pag" la em cima com letra maiscula, existiam outros erros, mas eram mais obvios