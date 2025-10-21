def Josephus(n, k):
    n = [x for x in range(1, n+1)]
    len_n = len(n) - 1
    i = -1
    n.pop(0)
    while len_n > 1:
        i = (i + k) % (len_n)
        n.pop(i)
        i -= 1
        len_n -= 1
    return n.pop(i)

while True:
    N = int(input())
    if N == 0: break
        
    k = 1
    result = 0
    while result != 13:
        result = Josephus(N, k)
        if result == 13: print(k); break
        k += 1
        