Inácio, dono de uma empresa de eletrodomésticos, estava preocupado com a quantidade de reclamações que seus produtos e serviços tinham na Internet. Por isso, resolveu criar um indicador para melhor acompanhar estas reclamações, o índice de insatisfação (ii) do cliente.

O índice de insatisfação, chamado de ii, é composto por vários outros índices, tais como, o índice de reclamação, o índice de indisponibilidade, além do número de cancelamentos, de acordo com a descrição a seguir.

Ele definiu que o índice de reclamações seria uma escala de 0 a 100. Se o cliente é atendido imediatamente após ligar ao call center zero é adicionado ao ii e 100 se esperam em média mais de 100 minutos para serem atendidos.  Se 60% ou mais das reclamações são resolvidas na primeira ligação, o ii baixa 5 pontos. Caso contrário aumenta 15 pontos.

Sobre o ii, é feita a seguinte alteração:

a) se o número de cancelamentos do serviços é maior ou igual a 10% do total dos clientes, o ii aumenta 80 pontos se o cancelamento foi por problemas nos serviços prestados ou diminui 30 pontos caso contrário.

b) se o número de cancelamentos dos serviços é menor do que 10% do total dos clientes, o ii aumenta 50 pontos se o cancelamento foi por problemas nos serviços prestados ou diminui 10 pontos caso contrário.

Depois disso, é computado o índice de indisponibilidade do serviço que varia de 0 a 100. Se os seus serviços ficaram fora do ar 10% ou mais do tempo em um mês, seu ii total será aumentado de 70 pontos, caso contrário, seu ii será rebaixado de 20 pontos.

Para isto, Inácio, que está aprendendo a programação, escreveu o seguinte programa em Python:

```py
indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

if (percentReclamResolPrim > 60):
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
print(f'{indice}')

if ( percentCliCancel <= 10):
    if (canceladoPorProblema==0):
        indice = indice + 80
    else:
        indice = indice - 30
else:
    if (canceladoPorProblema==0):
        indice = indice + 50
    else:
        indice = indice - 10
print(f'{index}');

if (indiceIndisponibilidade> 10):
    indice = indice - 70
else:
    indice = indice + 20
print(f'{indice}');
```

Corrija os erros do programa sabendo que:

A Entrada consiste de 5 valores inteiros, um por linha:
* o índice de reclamações;  
* a porcentagem das reclamações resolvidas na primeira ligação;
* a porcentagem dos clientes que solicitaram o cancelamento;
* o índice de disponibilidade; e 
* um número inteiro que pode ser 0 ou 1, conforme se segue:
    * 1 - cancelamento por problemas no serviço;
    * 0 - caso contrário.

A Saída deve apresenta três valores inteiros, um por linha:
* o índice de insatisfação da empresa levando-se em conta o índice de reclamações e a porcentagem de reclamações resolvidas na primeira ligação
* o ii final, depois de computado o índice de disponibilidade
* o valor da ii computando os cancelamentos e seus motivos.
