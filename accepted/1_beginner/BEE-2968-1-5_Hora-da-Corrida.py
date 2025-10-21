V, N = map(int, input().split())

ans = []
total = V * N
for n in range(1, 10):
    curr = round(total * 0.1 * n, 1)
    curr = int(curr) if curr.is_integer() else int(curr) + 1
    ans.append(str(curr))

print(' '.join(ans))