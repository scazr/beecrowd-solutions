while True:
    A, C = map(int, input().split())

    if A == 0 and C == 0: break

    X = list(map(int, input().split()))
    X.append(A)

    turned = 0
    for i in range(1, len(X)):
        if X[i-1] < X[i]: turned += X[i] - X[i-1] 

    print(turned)