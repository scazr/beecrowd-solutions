def rec(N, V, t):
    sqr = V * V
    if V == 0: return False

    if t >= N: return False
    if t + sqr >= N and (t - N) % V == 0: return True
    else: return rec(N, V-1, t + sqr)

while True:
    N, V = map(int, input().split())
    if N == V == 0: break

    if V >= N: print('possivel')
    else:
        res = False
        for v in range(V, 0, -1):
            res = rec(N, v, 0)
            if res == True: break
        print('possivel' if res else 'impossivel')