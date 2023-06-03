# porque bolacha e não biscoito
def pacotesDeBolacha(m,n,k):
    totalcomem = n * k
    if m < totalcomem:
        resto = m % n
    else:
        resto = m - totalcomem
    print(resto)

pacotesDeBolacha()

# m = total de pacotes de biscoito
# n = total de alunos
# k = quanto que cada aluno come