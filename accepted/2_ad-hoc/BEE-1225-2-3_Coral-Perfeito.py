while True:
    try:
        N = int(input())
        NOTES = list(map(int, input().split()))

        mean = sum(NOTES) / N
        if not mean.is_integer(): print(-1); continue
        mean = int(mean)

        min_bar = 1
        for note in NOTES:
            if note > mean:
                min_bar += note - mean

        print(min_bar)

    except EOFError: break
