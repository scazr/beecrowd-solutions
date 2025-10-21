from collections import Counter
from itertools import takewhile
while True:
    N, M = map(int, input().split())
    if N == M == 0: break
    total = Counter()
    for n in range(N):
        total.update(list(map(int, input().split())))
    
    mostCommon = total.most_common()[1:]
    second = mostCommon[0][1]

    print(' '.join(map(str, sorted(map(lambda x : x[0], takewhile(lambda x : x[1] == second, mostCommon))))) + ' ')

