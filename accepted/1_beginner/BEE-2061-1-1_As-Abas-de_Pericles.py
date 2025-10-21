N, M = map(int, input().split())
for m in range(M):
    ACTION = input()
    if ACTION[0] == 'f': N += 1
    else: N -= 1
print(N)