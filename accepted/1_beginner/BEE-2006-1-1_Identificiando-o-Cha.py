T = int(input())
n = list(map(int, input().split()))
OUTPUT = 0
for _ in n:
    if _ == T: OUTPUT += 1

print(OUTPUT)
