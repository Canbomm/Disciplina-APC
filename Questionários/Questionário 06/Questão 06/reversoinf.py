# Fiz com base no "Reverso 2", apenas para testar vários casos de maneira rápida

def inverteneg(a):
    # modulo = int((a**2)**(1/2))
    modulo = int(str(a)[1:])
    resultado = inverte(modulo)
    # adicionando o sinal de negativo novamente
    resultadof = "-" + str(resultado)
    resultadof = int(resultadof)
    return resultadof

def inverte(a):
    if a == 0:
        return 0
    else:
        # pegando a ultima casa e botando na primeira posição
        qcasas = len(str(a))
        ultimac = a%10
        invertido = ultimac * (10**(qcasas-1))
        # tratar o número pra poder adicionar a recursividade
        tratado = int((a-ultimac)/10)
        resultado = inverte(tratado)
        # somar o valor pra obter apenas um resultado
        resultado += invertido
        return resultado

# para testar valores do meu "Reverso 2"
n = 1
while n != 0:
    n = int(input("Digite um número:\n"))

    if n >= 0:
        answ = inverte(n)
    else:
        answ = inverteneg(n)

    print(answ)
