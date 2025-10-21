def dijikstra(start):
    visited = [False for n in range(N)]
    distance = [float('inf') for n in range(N)]

    distance[start] = 0
    queue = []
    queue.append((start, 0))
    len_queue = len(queue)

    while len_queue != 0:
        idx, min_value = queue.pop(0)
        len_queue -= 1

        visited[idx] = True

        if distance[idx] < min_value: continue
        
        for ptr_edge in range(N):
            edge = graph[idx][ptr_edge]    
            if edge == -1: continue
            
            new_distance = distance[idx] + edge

            if new_distance < distance[ptr_edge]:
                distance[ptr_edge] = new_distance
                queue.append((ptr_edge, new_distance))
                len_queue += 1

    return distance


while True:
    N, E = map(int, input().split())
    if N == 0 and E == 0: break

    graph = [[-1 for n in range(N)] for n2 in range(N)]

    for e in range(E):
        Y, X, H = map(int, input().split())
        Y -= 1; X -= 1
        if graph[X][Y] != -1: graph[X][Y] = 0; graph[Y][X] = 0
        else: graph[Y][X] = H

    K = int(input())
    
    for k in range(K):
        O, D = map(int, input().split())
        O -= 1; D -= 1
        
        result = dijikstra(O)[D]
        print(result if result != float('inf') else 'Nao e possivel entregar a carta')
    
    print()