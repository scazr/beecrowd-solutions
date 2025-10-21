OUTPUT = []

for N in range(int(input())):
    M = int(input())

    P = list(map(int, input().split()))
    PSorted = sorted(P, reverse=True)

    unchanged = 0
    for _ in range(M):
        if PSorted[_] == P[_]: unchanged += 1

    OUTPUT.append(unchanged)

for _ in OUTPUT: print(_)
