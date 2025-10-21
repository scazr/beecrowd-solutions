while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0: break
    
    C = list(map(int, input().split()))
    
    D = [0 for b in range(B)]
    for n in range(N):
        debenture = tuple(map(int, input().split()))
        D[debenture[0] - 1] += debenture[2]
        C[debenture[1] - 1] += debenture[2]
    
    result = 'S'
    for bank in range(B):
        if D[bank] > C[bank]: result = 'N'; break
    
    print(result)