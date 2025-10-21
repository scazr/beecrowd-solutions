while True:
    H = int(input())
    if H == 0: break
    maxH = H
    while H > 1:
        H = H >> 1 if H % 2 == 0 else (3 * H) + 1
        maxH = max(maxH, H)
    print(maxH)