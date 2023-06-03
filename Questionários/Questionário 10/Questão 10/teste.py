lido = ["swqoozotpbgwxflghgrl",
"eebrjrkjktjibnmjfzvz",
"gekcoonokalzoekctfqq",
"cxaufxwxvuuqozsdsdgq",
"tawoxlfwmnxlqmwqcglw",
"pjvgjxxdmcbarkxqkqma",
"xqjrgtmdrdabxfplicsl",
"bicxyyssnsrzvbfcdmal",
"lejbtqnwfvfckzuejsay",
"rkzujukgrfrjiniafxaz",
"tikfrkrimwjaiykdmuog",
"vziiapkmalbwsyoncnoe",
"bjuwinbhjqksgukhjcfp",
"ueuwfiqsgqkjssosceah",
"jccmpcvrpjivubibeibz"]

lido = ['nkkumvqgqnmjime', 'zewafngwhnmbkur', 'rrwlnzivkwmjpfg', 'tjkrnpbkzzrjygz', 'exisgsklariuzdz', 'yyuyajqaupezdir', 'ktlreetkdkwatlw', 'onkautaklveqkhi', 'iolwamelvydsdqk', 'svjotctfkenwjab', 'sxmjtyoqnamgiis', 'ludjenlyihavzbp', 'uupujosxbcwally', 'lbbhcrjglhqubgg', 'cakoswwoflqhljt']

def achaHorizon(lista,palavra):
    for index1, linha in enumerate(lista):
        for index2, char in enumerate(linha):
            if char == palavra[0]:
                procurando = linha[index2:index2+5]
                if procurando == palavra:
                    return True, index1+1, index2+1
    return False, index1+1, index2+1

def transposta(lista):
    transposta = []
    for i1 in range(0,len(lista[0])):
        nova_linha = ""
        for i2 in range(0,len(lista)):
            elemento = lista[i2][i1]
            nova_linha += elemento
        transposta.append(nova_linha)
    return transposta

horizontal = achaHorizon(lido,"wally")
if horizontal[0]:
    print(f"{horizontal[1]} {horizontal[2]} horizontal")
else:
    transposta = transposta(lido)
    vertical = achaHorizon(transposta,"wally")
    print(f"{vertical[2]} {vertical[1]} vertical")
