import csv

cursos = { '127' : 'Bacharelado em Ciência da Computação',
'132' : 'Arquitetura e Urbanismo',
'136' : 'Engenharia Civil',
'137' : 'Engenharia Elétrica',
'139' : 'Engenharia Florestal',
'158' : 'Licenciatura em Física',
'159' : 'Licenciatura em Química',
'160' : 'Licenciatura em Ciências Biológicas',
'161' : 'Licenciatura em Matemática',
'162' : 'Licenciatura em Lígua Portuguesa'
}

filename = input()
f = open(filename, 'r', encoding='latin_1', newline='')
reader = csv.reader(f, delimiter=';')
soma = 0
cont = 0
total = -1
total_M = 0
total_F = 0
for row in reader:
    total += 1
    if row[4]=="555": 
        curso = row[1]
        cont += 1
        numero,decimal = row[5].split(",")
        soma += float(numero + str(int(decimal)/10)[1:])
    if row[3] == 'M':
        total_M += 1
    elif row[3] == 'F':
        total_F += 1
if cont == 0:
    media = 0
else:
    media = soma / cont
print(f'Relatório ENADE 2017')
print(f'Curso: {cursos[row[1]]}')
print(f'Total de alunos inscritos: {total}') #não conta a primeira linha que é o sigla dos campos
print(f'Total de alunos que realizaram o Enade: {cont}')
print(f'Quantidade de alunos do sexo masculino do curso inscritos no ENADE: {total_M}')
print(f'Quantidade de alunos do sexo feminino do curso inscritos no ENADE: {total_F}')
print(f'Média geral dos alunos que realizaram o ENADE: {media:.2f}')
f.close()
