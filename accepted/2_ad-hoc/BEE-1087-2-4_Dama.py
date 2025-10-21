while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0: break

    dX, dY = X1 - X2, Y1 - Y2
    if dX == 0 and dY == 0: print(0); continue

    if dX < 0: dX = -dX
    if dY < 0: dY = -dY

    if X1 == X2 or Y1 == Y2 or dX == dY: print(1); continue
    else: print(2); continue