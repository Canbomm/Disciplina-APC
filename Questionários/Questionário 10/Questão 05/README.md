Os arquivos Comma-separated Values, também conhecidos como CSV, são arquivos de texto de formato regulamentado pelo RFC 4180, cuja ideia é listar uma sequência de valores por linha, separando-os por vírgulas. É um formato muito utilizado para organizar informações. Como no Brasil a parte decimal de um número é separada por vírgula da parte inteira, usa-se o ponto-e-vírgula como separador

Um exemplo de conteúdo de um arquivo CSV, pode ser visto abaixo:

CO_IES;CO_CURSO;NU_IDADE;TP_SEXO;TP_PRES;NT_GER;QE_I41;QE_I56;QE_I59;QE_I60;QE_I69;QE_I70
2;160;25;F;222;;;;;;;
2;160;21;M;555;79,8;6;4;5;3;B;J
2;160;21;F;555;64,6;6;6;6;6;A;C
No exemplo temos o extrato do arquivo CSV do ENADE 2017 do curso de Licenciatura em Ciências Biológicas (CO-CURSO = 160) da UnB (CO_IES = 2).
O exemplo consiste de algumas linhas co alguns campos do arquvo .csv original. O significado dos campos e os valores que eles podem receber estão no arquivo Excel https://aprender3.unb.br/pluginfile.php/1595919/question/questiontext/1535338/5/19525113/Dicion%C3%A1rio%20de%20vari%C3%A1veis%20dos%20Microdados%20do%20Enade_Edi%C3%A7%C3%A3o%202017.xlsx

Para isto, Cicrano da Silva, que está aprendendo a programar, fez um programa para ler o conteúdo de um arquivo CSV do ENADE 2017 e gerar um relatório. No entanto, seu programa contém alguns erros. Ajude ele a debuggar o programa!

```py
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
total = 0
total_M = 0
total_F = 0
for row in reader:
    total += 1
    if row[5]=="555": 
        curso = row[1]
        cont += 1
        soma += float(row[5])
    if row[3] == 'M':
        total_M += 1
    elif row[3] == 'F':
        total_F += 1
media = soma / cont
print(f'Relatório ENADE 2017')
print(f'Curso: {cursos[curso]}')
print(f'Total de alunos inscritos: {total}') #não conta a primeira linha que é o sigla dos campos
print(f'Total de alunos que realizaram o Enade: {cont}')
print(f'Quantidade de alunos do sexo masculino do curso inscritos no ENADE: {total_M}')
print(f'Quantidade de alunos do sexo feminino do curso inscritos no ENADE: {total_F}')
print(f'Média geral dos alunos que realizaram o ENADE: {media:.2f}')
```
