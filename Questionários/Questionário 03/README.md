**Exercícios retirados do Questionário 3 (Funções) 2022**

1. Implemente uma função chamada powAPC que calcule XY. Sua função deve receber os valores de X e Y, ambos inteiros, e imprimir o valor de Xy em ponto flutuante.

2. Elabore um programa que troca a ordem de apresentação de dois números, de um total de 5 pares de números. Seu programa deve ler 5 pares de números inteiros e para cada um deles deverão ser impressos os números com a ordem trocada. A função responsável por realizar essa operação deverá chamar trocarAB e receber dois valores numéricos. 

3. Descobrir um valor que dê a data de depois de amanhã:
```py
from datetime import date
from datetime import timedelta
t = int(input())
data1 = date.today()
data2= data1 - timedelta(days = t)
print(data2)
```

4. Elabore duas funções gato e cachorro. A função gato simula o acordar de um gato e deve apresentar duas mensagens, uma em cada linha: "miaaaaau, acordei" e "acorda cachorro, sao h horas da manha" onde h é uma variável passada como argumento na função gato e representa a hora atual. A função cachorro (que é acordado pelo gato) é chamada e apresenta a mensagem "au auuuuu acordei".

5. (pulei a contextualização) Durante sua viagem, Bonifácio planeja utilizar todos os seus jogos de vestimenta country, mas com a restrição de que ele veste um jogo apenas uma única vez e que não há distinção entre os chapéus e os pares de botas. Sabe-se que Bonifácio possui em sua coleção de vestimentas x pares de botas e y chapéus, elabore uma função vestimentas que receba os dois números inteiros x e y como parâmetros e calcule a quantidade máxima de peças nos jogos de vestimentas country m que Bonifácio levará em sua bagagem.
   
6. Brincando com números by "Gael" (essa questão é muito grande pra eu botar aqui, iria ficar um BLOCO de texto). Basicamente me deram um monte de operações que uma pessoa estava tentando fazer e me pediram pra "otimizar" o código dessa pessoa, é bem fácil de entender quando você olha o código que eu acabei criando.

7. O programa abaixo imprime a hipotenusa de um triângulo dados os seus catetos. Ao executar esse programa, é possível perceber que ele apresenta alguns erros. Analise o código e faça os ajustes necessários para que ele funcione corretamente. É necessário realizar mais de uma alteração para que ele funcione de acordo com os exemplos disponibilizados.
```py
def pitagoras(b, c):
    a = (b*b + c*c)**0.5
    print(a)

b, c = input().split()
Pitagoras(b, c)
```

8. (pulei a contextualização) Seu número preferido é 3 e por isso ele gosta sempre de ter 3 opções disponíveis. Dessa forma, sua tarefa é elaborar um Programa para imprimir como a piscina ficaria com cada uma das três opções de comprimento. No seu programa você deve implementar uma função chamada print_rectangle que recebe esse valor e imprime a piscina.

9. O prof. Fagundes comprou uma caixa com m pacotes de bolacha recheada para distribuí-los igualmente entre os n alunos da sua turma de Estruturas de Dados na Universidade de Brasília (UnB). Apesar dos alunos terem adorado essa surpresa, cada um consegue comer no máximo k pacotes de bolacha, portanto, alguns desses pacotes entregues por aluno podem sobrar. A generosa ideia do querido professor consiste em pegar esses pacotes restantes e entregá-los aos funcionários do Departamento de Ciência da Computação (CIC) da UnB.

10. O programa a seguir gera um padrão geométrico formados por 4 caracteres dispostos em 9 linhas, cada linha com 9 caracteres usando-se apenas as instruções e outros recursos que aprendemos até agora. Corrija os erros de sintaxe e de lógica para que ele imprima o padrão corretamente apenas usando o que foi ensinado até o momento.