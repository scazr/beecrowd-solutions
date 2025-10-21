while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0: break

    X = set(map(int, input().split()))
    Y = set(map(int, input().split()))
    
    print(min(len(X.difference(Y)), len(Y.difference(X))))
    