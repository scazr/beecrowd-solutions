N = int(input())
carlos = int(input())
candidates = [int(input()) for n in range(N-1)]

for candidate in candidates:
    if candidate > carlos: print('N'); break
else:
    print('S')