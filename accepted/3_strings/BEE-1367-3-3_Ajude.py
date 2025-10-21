while True:
    N = int(input())
    if N == 0: break

    tries = dict()
    S = 0
    P = 0

    for n in range(N):
        L, T, C = input().split()
        T = int(T)

        if C[0] == 'i':
            tries[L] = tries.setdefault(L, 0) + 20
        elif C[0] == 'c':
            P += tries.setdefault(L, 0) + T
            S += 1
    print(S, P)
          