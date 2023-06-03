Um número é considerado um número de Armstrong de ordem N se for igual à soma de seus dígitos elevados a potência de N, onde N é a quantidade de dígitos do número.

Em outras palavras um inteiro positivo é chamado número de Armstrong de ordem N se:

abcd... = an + bn + cn + dn + ...
Sabendo dessa definição, desenvolva um programa que verifique se um dado número é um número de Armstrong de ordem N ou não. Cada etapa dos cálculos para decidir se o número é ou não de Armstrong deve ser mostrada seguindo o modelo (o número 153 será usado como exemplo):

3^3 + 5^3 + 1^3 = 
27 + 125 + 1 = 153
153 é um número de Armstrong de 3 ordem.

Na primeira linha devem ser exibidos os dígitos do número de entrada n, do último ao primeiro, elevados à quantidade de dígitos N, com um sinal de igualdade no final.
Na segunda linha devem ser exibidos os resultados das operações de potenciação sobre cada dígito somado seguido de um sinal de igualdade e o número de entrada caso sejam iguais ou de desigualdade e o número de entrada caso sejam diferentes.
Na última linha deve ser exibida a mensagem "n é um número de Armstrong de N ordem." caso o número de entrada seja um número de Armstrong de N ordem ou "n não é um número de Armstrong de N ordem." caso o número de entrada não seja um número de Armstrong de N ordem, onde n é o número de entrada e N é a quantidade de dígitos do número de entrada.