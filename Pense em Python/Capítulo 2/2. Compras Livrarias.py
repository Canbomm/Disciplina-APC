#Entrada
preco_livro = float(input("Qual o preço de apenas um livro?\n"))
desconto = float(input("Qual o desconto (não coloque o sinal de porcentagem)?\n"))
frete_solo = float(input("Qual o valor do frete para apenas uma unidade?\n"))
frete_unidade = float(input("Existe um outro valor de frete ao comprar mais de uma unidade?\n"))
livros = int(input("Quantos livros a livraria pretende comprar?\n"))

#Computacao
frete = frete_solo + frete_unidade * (livros - 1)
descontototal = (100 - desconto)/100
preco_livro_desc = (preco_livro * descontototal) * livros
preco_total = preco_livro_desc + frete

#Saida
print(f"O total deverá estar por volta de: R${preco_total:.2f}")
