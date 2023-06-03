def collatz(s, n, cont):
    if cont < n:
        if s % 2 == 0: #é par
            clltz = int(s/2)
        else:
            clltz = 3*s - 1
        return collatz(clltz, n, cont+1)
    else:
        return s

print(collatz(12, 5, 1))