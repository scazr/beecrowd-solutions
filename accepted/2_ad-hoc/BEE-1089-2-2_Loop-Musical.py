while True:
    if int(input()) == 0: break

    H = tuple(map(int, input().split()))
    lenH = len(H)
    
    peaks = 0
    
    if (H[lenH - 1] > H[0] and H[0] < H[1]) or (H[lenH - 1] < H[0] and H[0] > H[1]): peaks += 1 #;print('a')
    for Hi in range(1, lenH - 1):
        if (H[Hi - 1] > H[Hi] and H[Hi] < H[Hi + 1]) or (H[Hi - 1] < H[Hi] and H[Hi] > H[Hi + 1]): peaks += 1 #;print('b')
    if (H[lenH - 2] > H[lenH - 1] and H[lenH - 1] < H[0]) or (H[lenH - 2] < H[lenH - 1] and H[lenH - 1] > H[0]): peaks += 1 #;print('c')
    
    print(peaks)