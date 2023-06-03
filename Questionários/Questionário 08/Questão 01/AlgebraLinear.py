dimensoes = int(input())
vetor1 = [int(e) for e in input().split()]
vetor2 = [int(e) for e in input().split()]

produtovetorial = []
for i in range(0,dimensoes):
    produtovetorial.append(vetor1[i] * vetor2[i])

# é ortogonal?
eortogonal = sum(produtovetorial)

if eortogonal == 0:
    print("ortogonais")
else:
    print(eortogonal)
