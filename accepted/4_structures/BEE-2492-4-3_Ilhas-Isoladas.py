while True:
    islands = dict()
    reverse = dict()
    T = int(input())
    if T == 0: break
    TS = [input() for t in range(T)]
    function = True
    invertible = True
    for t in TS:
        X, Y = t.split(' -> ')
        if islands.get(X) != None: function = False
        if reverse.get(Y) != None: invertible = False
        islands[X] = Y
        reverse[Y] = X

    if not function: print('Not a function.')
    elif not invertible: print('Not invertible.')
    else: print('Invertible.')