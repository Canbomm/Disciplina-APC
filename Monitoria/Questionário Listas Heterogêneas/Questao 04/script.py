totalmercearias, mangos, totalprodutos = [int(x) for x in input().split()]
produtos = [int(x) for x in input().split()]

mercearias = []
for i in range(0,totalmercearias):
    mercearias.append([int(x) for x in input().split()])

indmercearia = 0
while mangos > 0:
    
