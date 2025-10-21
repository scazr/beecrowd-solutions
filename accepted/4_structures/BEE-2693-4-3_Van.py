while True:
    try:
        Q = int(input())
        ASC = [input().split() for q in range(Q)]
        pq = map(lambda x : (int(x[2]), x[1], x[0]), ASC)
        for q in sorted(pq):
            print(q[2])
            
    except EOFError: break