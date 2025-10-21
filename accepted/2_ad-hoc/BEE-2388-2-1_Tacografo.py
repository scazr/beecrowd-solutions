N = int(input())

deltaS = 0

for _ in range(N):
    T, V = map(int, input().split())
    deltaS += T * V
    
print(deltaS)
