N, S = map(int, input().split())
lowest = S
for D in range(N):
    move = int(input())
    if (S := S + move) < lowest: lowest = S
print(lowest)
