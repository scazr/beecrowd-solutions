N, M = map(int, input().split())
swapMap = dict()
for n in range(N):
    E, S = input().split()
    swapMap[E] = S
    swapMap[S] = E

for m in range(M):
    print(''.join(map(lambda x : swapMap.get(x, x), input())))