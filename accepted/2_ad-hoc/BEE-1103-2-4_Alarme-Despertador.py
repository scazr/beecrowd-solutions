while True:
    H1, M1, H2, M2 = map(int, input().split())

    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0: break
    
    MT1 = (H1 * 60) + M1
    MT2 = (H2 * 60) + M2

    if MT1 > MT2: print(1440 - (MT1 - MT2))
    else: print(((H2 * 60) + M2) - ((H1 * 60) + M1))