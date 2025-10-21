import sys

def find_n():
    if not contains[0] or not contains[N]: return 'N'
    for b in range(0, N + 1):
        for i in range(0, N - b + 1):
            if contains[i] and contains[i + b]: break
        else:
            return 'N'
    return 'Y'
    
while True:
    N, B = map(int, input().split())
    if N == 0 and B == 0: break

    b = [int(n) for n in input().split()]

    contains = [False for i in range(N + 1)]
    for i in b:
        contains[i] = True

    print(find_n())