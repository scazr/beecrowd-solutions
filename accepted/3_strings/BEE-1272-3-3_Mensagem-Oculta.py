while True:
    try:
        N = int(input())
        for n in range(N):
            WORDS = ' '.join(input().split('·')).split()

            for word in WORDS:
                print(word[0], end='')
            print()

    except EOFError:
        break