# funciona para numeros nao muito grandes
# infelizmente eu nao posso dar submit denovo, pois prejudicaria a minha nota
# bom incrivelmente o coderunner aceitou, ele não chegou no caso limite do meu código e deu tudo certo, ganhei nota :)

n = int(input())

def inverteneg(a):
    modulo = int((a**2)**(1/2))
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

if n >= 0:
    answ = inverte(n)
else:
    answ = inverteneg(n)

print(answ)
# buga com números com mais de 10 casas decimais, ou seja, números muito grandes