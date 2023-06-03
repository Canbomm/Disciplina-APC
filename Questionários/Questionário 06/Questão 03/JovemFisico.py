# quantidade de vetores
qvetores = int(input())
i,j,k = 0,0,0

while qvetores > 0:
    qvetores -= 1
    ni,nj,nk = map(int,input().split())
    i += ni
    j += nj
    k += nk

if i == 0 and j == 0 and k == 0:
    print("YES")
else:
    print("NO")
