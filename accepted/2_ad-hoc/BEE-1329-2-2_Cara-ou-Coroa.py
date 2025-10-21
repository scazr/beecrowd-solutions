while True:
    N = int(input())
    if N == 0: break

    R = tuple(map(int, input().split()))

    mary, john = 0, 0
    for r in R:
        if r == 0: mary += 1
        else: john += 1

    print(f"Mary won {mary} times and John won {john} times")