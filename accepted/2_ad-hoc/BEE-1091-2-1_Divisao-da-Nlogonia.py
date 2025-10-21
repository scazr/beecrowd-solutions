while True:
    K = int(input())
    if K == 0: break

    N, M = map(int, input().split())

    for k in range(K):
        X, Y = map(int, input().split())

        if X == N or Y == M: print('divisa')
        else:
            posX = None
            posY = None
        
            if M < Y: posY = 'N'
            else: posY = 'S'
            
            if N < X: posX = 'E'
            else: posX = 'O'
            
            print(f"{posY}{posX}")