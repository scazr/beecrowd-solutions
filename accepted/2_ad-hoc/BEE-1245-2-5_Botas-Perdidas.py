while True:
    try:
        N = int(input())
        
        e_boots = [0 for n in range(61 - 30)]
        d_boots = [0 for n in range(61 - 30)]

        for n in range(N):
            boot = input().split()

            if boot[1] == 'E': e_boots[int(boot[0]) - 30] += 1
            else: d_boots[int(boot[0]) - 30] += 1
        
        max_pairs = 0
        for n in range(61-30): max_pairs += min(e_boots[n], d_boots[n])

        print(max_pairs)

    except EOFError: break