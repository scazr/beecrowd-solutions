N, C, T = map(int, input().split())
family_tree = {}
for _ in range(C):
    parent1, parent2, son = input().split()

    if not son in family_tree: family_tree[son] = {parent1, parent2}
    if not parent1 in family_tree: family_tree[parent1] = set()
    if not parent2 in family_tree: family_tree[parent2] = set()

def DFS(son):
    queue, visited = [son], dict(((key, False) for key in family_tree))
    for horse in queue:
        if not visited[horse]:
            for parent in family_tree[horse]:
                queue.append(parent)
            visited[horse] = True

    return list(filter(lambda key: visited[key], visited))

for _ in range(T):
    son1, son2 = input().split()
    a, b = DFS(son1), DFS(son2)
    relation = False
    for parent1 in a:
        for parent2 in b:
            if parent1 == parent2: relation = True; break;
    print("verdadeiro" if relation else "falso")