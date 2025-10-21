import re
N = int(input())
OUTPUT = []

def sim(N, D):
    if N > D: m = N
    else: m = D
    while m != 1:
        if N % m == 0 and D % m == 0:
            N /= m; D /=m
            break
        m -= 1
    return str(int(N)) + "/" + str(int(D))
            

for _ in range(0, N):
    INPUT = input().split()
    X = " ".join(INPUT[0:3])
    op= INPUT[3]
    Y = " ".join(INPUT[4:7])
    N1, D1 = map(int, re.split("\s/\s", X))
    N2, D2 = map(int, re.split("\s/\s", Y))

    if   op == "+": OUTPUT.append(str(N1*D2+N2*D1) + "/" + str(D1*D2) + " = " + str(sim(N1*D2+N2*D1, D1*D2)))
    elif op == "-": OUTPUT.append(str(N1*D2-N2*D1) + "/" + str(D1*D2) + " = " + sim(N1*D2-N2*D1, D1*D2))
    elif op == "*": OUTPUT.append(str(N1*N2) + "/" + str(D1*D2) + " = " + sim(N1*N2, D1*D2))
    elif op == "/": OUTPUT.append(str(N1*D2) + "/" + str(N2*D1) + " = " + sim(N1*D2, N2*D1))


for _ in OUTPUT: print(_)
