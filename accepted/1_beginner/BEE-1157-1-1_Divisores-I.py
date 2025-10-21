INPUT = int(input())
for n in range(1, int(INPUT) + 1, 1+ INPUT % 2):
    if INPUT % n == 0: print(n)