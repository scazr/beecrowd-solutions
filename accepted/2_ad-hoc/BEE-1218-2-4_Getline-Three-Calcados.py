loop = 1
while True:
    try:
        N = int(input())
        SHOES = input().split()
        temp_SHOES = [[int(SHOES[x]), SHOES[x+1]] for x in range(0, len(SHOES), 2)]
        SHOES = temp_SHOES

        F, M = 0, 0
        for m in SHOES:
            if m[0] == N:
                if m[1] == 'F': F += 1
                elif m[1] == 'M': M += 1
        
        if loop > 1: print()
        
        print(f'Caso {loop}:')
        print(f'Pares Iguais: {F + M}')
        print(f'F: {F}')
        print(f'M: {M}')

        loop += 1

    except EOFError: break