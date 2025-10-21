N = int(input())
V = []
OUTPUT = 0

for _ in range(N):
    V.append(int(input()))
    if _ != 0 and V[_] != V[_-1]: OUTPUT += 1

print(OUTPUT + 1)
        
