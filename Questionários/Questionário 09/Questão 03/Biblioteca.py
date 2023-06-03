biblioteca = {}
repeticao = 5

while repeticao > 0:
    livro = input()
    quantidade = int(input())
    biblioteca[livro] = quantidade
    repeticao -= 1

busca = input()

try:
    print(f"Achei! Temos {biblioteca[busca]} exemplar(es)!")
except:
    print(f"Poxa, não temos esse livro")
