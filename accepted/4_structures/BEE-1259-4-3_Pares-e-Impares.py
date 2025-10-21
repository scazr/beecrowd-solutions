numbers = []
for cases in range(0, int(input())):
    numbers.append(int(input()))

even = sorted(list(filter(lambda _: _ % 2 == 0, numbers)))
odd  = sorted(list(filter(lambda _: _ % 2 == 1, numbers)), reverse=True)

for _ in even + odd: print(_)
