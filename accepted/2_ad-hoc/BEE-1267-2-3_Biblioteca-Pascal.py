while True:
    N, D = map(int, input().split())
    if N == 0 and D == 0: break

    attendance = [True for n in range(N)]
    n_att = N
    for d in range(D):
        Ns = list(map(int, input().split()))

        for n in range(N):

            if not attendance: continue
            
            elif attendance[n] and not Ns[n]:
                attendance[n] = False
                n_att -= 1

    if n_att <= 0: print('no')
    else: print('yes')