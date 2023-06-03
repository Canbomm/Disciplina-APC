**Exercícios retirados do Questionário 4 (Condicionais e Recursividade) 2022**

1. Implemente uma função chamada area que imprime a área de uma determina figura geométrica. A função deve receber 3 parâmetros, sendo dois deles valores numéricos e uma string representando a forma geométrica. A área da figura deve ser do tipo inteiro. As formas geométricas permitidas são retangulo, losango, triangulo e circulo.
   
2. Escreva uma função chamada older(ageA, ageB) que receberá a idade em anos completos dos filhos A e B e deverá imprimir A se o filho A for com certeza mais velho, B se o filho B for com certeza mais velho e Maybe twins se não for possível saber com certeza quem é o mais velho.
   
3. Na loja de Laiane o parcelamento funciona de uma maneira diferente: o valor da parcela não possui centavos, assim como o valor de qualquer produto dessa loja. Sendo assim, se a compra ficou em 355 reais e esta for parcelada em quatro vezes, as parcelas serão de 88 reais e o restante do valor deve ser pago no ato da compra, ou seja, o cliente pagará à vista 3 reais e dividirá 352 reais em quatro vezes de 88 reais. Todavia, para um cliente afiliado o que ocorre é que ele não precisa pagar o resto, isto é, ele faz uma compra de 355 reais, parcela em 4 vezes e tem um desconto de 3 reais, pagando apenas 352.
Laiane resolveu que essa semana dará esse desconto para qualquer cliente, sendo filiado ou não, nas compras a partir de 350 reais.

4. Implemente uma função recursiva chamada imprimeTermos que receba um número inteiro n e imprima os termos da sequência n,n−2,n−4,...,0, isto é, os termos da sequência que começa pelo valor n e termina em 0, decrescendo de 2 em 2 valores.

5. (pulei a contextualização) Além disso, Batatinha só vai atrás da bolinha se a distância entre ele e a bola for menor ou igual que k metros. Se a bolinha estiver a menos de k metros de distância, Batatinha diz *miau* ta bom, vou buscar e vai buscar a bolinha. Se ela estiver a exatamente k metros, ele diz pfff... ta bom. Se estiver a mais do que k metros, ele diz ta achando que eu sou cachorro? e olha de cara feia para Johnin.

6. Para que seja uma corrida justa, os dois irmãos sempre param ao mesmo tempo para descansar. Eles param pra descansar quando Jorge está na posição j×3 e Giovani na posição g×2, onde j e g são as posições que eles estavam na última vez que descansaram, ou a posição que estavam no início da corrida. Isso sempre acontece porque Jorge tem as pernas maiores que as de Giovani, então ele corre mais rápido. A corrida acaba quando o irmão mais velho ultrapassa o mais novo.

7. Uma loja de informática esta promovendo a venda de 2 produtos: laptops a 1500 reais cada, e ipads a 1000 reais cada.
Se o cliente comprar 3 ou mais unidades, entre laptops e ipads, a loja desconta 500 reais.
Sobre o valor resultante, a loja dá um desconto ou acréscimo que depende da forma de pagamento:

    Se o cliente pagar a vista:

        a) entre os dias 1 e 15, o desconto será de 10%.

        b) entre os dias 16 e 31, o desconto será de 5%.

    Se o cliente pagar a prazo:

        a) entre os dias 1 e 15, o acréscimo será de 8%.

        b) entre os dias 16 e 31, o acréscimo será de 10%.

    Sobre o valor resultante, será cobrado o frete, que depende da distância da entrega:

        a) se a distância for menor ou igual a 50 km, o frete será de 100 reais;

        b) se a distância for maior que 50 km, o frete será de 200 reais.
    
    O dono da loja, que está aprendendo a programar, fez o programa abaixo:
    ```py
    lap, ipa, dia, pag; dis = input().split()
    lap = int(lap)
    ipa = int(ipa)
    dia = int(dia)
    Pag = int(pag)
    dis = int(dis)

    valor = lap * 1500 + ipa * 1000;

    if ((lap + ipa) > 3):
        valor = valor - 500
        
    if (pag == 0):
        if (dia >= 16):
            valor = valor * 1.90
        else:
            valor = valor * 1.95
    else:
        if (dia > 15):
            valor = valor * 1.08
        else:
            valor = valor * 1.10
            
    if (dis=50):
        valor = valor + 100
    else:
        valor = valor + 200

    print(f'{valor:.2f}')
    ```

8. Em Campinas, cidade do interior de São Paulo, existem infinitos galões de água de 1 litro, que custam a dinheiros, e infinitos galões de 2 litros, que custam b dinheiros, disponíveis para venda. Qual o menor número de dinheiros necessário para Fagundes comprar exatamente n litros de água?

9. (pulei a contextualização) "A partir de qualquer número n, dividindo-o por 2 se for par, ou multiplicando por 3 e adicionando 1 se for ímpar, e fazendo assim sucessivamente, chegaremos sempre ao número 1".

10. (pulei a contextualização) Primeiramente, é preciso ter todas as notas das 3 provas que ocorreram durante o semestre. Ele então verifica as 3 notas de um aluno e se assegura de que todas são maiores ou iguais a 5. Caso qualquer uma das notas esteja abaixo de 5 o aluno será reprovado. Caso todas as notas sejam maiores ou iguais a 5 o aluno será aprovado. Por fim, ele verifica em ordem as notas das 3 provas, classificando-as sob o sistema de menções da UNB em MM, MS e SS. Dai ele fez o seguinte código:
    ```py
    entradas = input().split()
    n1 = int(entradas[0])
    n2 = int(entradas[1])
    n3 = int(entradas[2])

    if n1 > 5 and n2 > 5 and n3 >5:
        print('APROVAR')
        
        #Cálculo da nota 1
        if n1 >= 5 and n1 < 7:
            print('Prova 1: MM')
        if n1 >= 7 and n1 < 9:
            print('Prova 2: MS')
        else:
            print('Prova 1: SS')
        #Cálculo da nota 2
        if n2 >= 5 and n2 < 7:
            print('Prova 2: MM')
        if n2 >= 7 and n2 < 9:
            print('Prova 2: MS')
        else:
            print('Prova 2: SS')
        #Cálculo da nota 3
        if n1 >= 5 and n1 < 7:
            print('Prova 2: MM')
        if n1 >= 7 and n1 < 9:
            print('Prova 2: MS')
        else:
            print('Prova 2: SS')
            
    else:
        print('REPROVAR')
    ```