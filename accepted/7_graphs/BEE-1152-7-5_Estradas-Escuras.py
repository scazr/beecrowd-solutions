def find(graph, parent, i):
        if parent[i] != i: parent[i] = find(graph, parent, parent[i]) 
        return parent[i]

def union(parent, rank, x, y): 
        if rank[x] < rank[y]: parent[x] = y 
        elif rank[x] > rank[y]: parent[y] = x 
  
        else: parent[y] = x; rank[x] += 1

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0: break

    graph = sorted([list(map(int, input().split())) for n in range(N)], key=lambda x : x[2])

    i, e = 0, 0

    result = []
    
    parent, rank = [], []
    for node in range(M): parent.append(node); rank.append(0) 

    while e < M - 1: 

        u, v, w = graph[i] 
        i = i + 1
        x = find(graph, parent, u)
        y = find(graph, parent, v)

        if x != y: 
            e = e + 1
            result.append([u, v, w]) 
            union(parent, rank, x, y) 
    
    minimumCost = 0
    totalCost = 0
    for u, v, weight in graph:
        totalCost += weight
    for u, v, weight in result: 
        minimumCost += weight
     
    print(totalCost - minimumCost) 
