biblioteca = {}
repeticao = 5

while repeticao > 0:
    livro = input()
    quantidade = int(input())
    biblioteca[livro] = quantidade
    repeticao -= 1

busca = input()

def procuraDic(string,dicionário):
    chaves = list(biblioteca.keys())
    for chave in chaves:
        if chave == string:
            return dicionário[chave]
    return ""

resultado = procuraDic(busca,biblioteca)
if resultado != "":
    print(f"Achei! Temos {resultado} exemplar(es)!")
else:
    print(f"Poxa, não temos esse livro")
