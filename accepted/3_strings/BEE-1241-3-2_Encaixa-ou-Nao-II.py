for n in range(int(input())):
    N1, N2 = input().split()
    
    encaixa = True
    len_N1 = len(N1)
    len_N2 = len(N2)

    if len_N1 < len_N2: encaixa = False
    else:
        for ch in range(-1, -len_N2-1, -1):
            if N1[ch] != N2[ch]: encaixa = False; break

    print('encaixa' if encaixa else 'nao encaixa')