def tem_letra_maiúscula(s):
    for letra in s:
        if letra.isupper():
            return True
    return False

def tem_letra_miniscula(s):
    for letra in s:
        if letra.islower():
            return True
    return False

def tem_numero(s):
    for caractere in s:
        unicode = ord(caractere)
        if unicode >= 48 and unicode <= 57:
            return True
    return False

def nao_tem_caractere_especial(s):
    for caractere in s:
        unicode = ord(caractere)
        if unicode >= 32 and unicode <= 47:
            return False
        elif unicode >= 58 and unicode <= 64:
            return False
        elif unicode >= 91 and unicode <= 96:
            return False
        elif unicode >= 123 and unicode <= 126:
            return False
    return True

senha = input()
tamanho = len(senha)

if tem_numero(senha) and tem_letra_maiúscula(senha) and tem_letra_miniscula(senha) and nao_tem_caractere_especial(senha) and tamanho >= 6 and tamanho <= 32:
    print(f"Senha valida.")
else:
    print(f"Senha invalida.")
