while True:
    N, C, K = map(int, input().split())

    if N == C == K == 0: break
    counter = dict()

    for k in range(1, K+1):
        counter[k] = 0

    for i in range(N):
        for j in map(int, input().split()):
            counter[j] += 1

    sorList = list(sorted(counter.items()))
    lc = sorList[0]
    filList = filter(lambda x : x[1] == lc[1], sorList)
    mapList = list(map(lambda x : str(x[0]), filList))
    print(' '.join(list(mapList)))
