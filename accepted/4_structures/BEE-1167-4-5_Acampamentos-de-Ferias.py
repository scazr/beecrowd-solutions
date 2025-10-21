while True:
    N = int(input())
    if N == 0: break
    
    children = []
    for n in range(N):
        NAME, VALUE = input().split()
        children.insert(0, (NAME, int(VALUE)))
        
    len_children = N
    first = True
    
    ptr = N - 1
    while ptr >= len_children: ptr -= len_children
    while ptr < 0: ptr += len_children
    popped = children[ptr]
    if popped[1] % 2 == 0: ptr += popped[1] 
    else: ptr -= popped[1]

    while len_children > 1:
        while ptr >= len_children: ptr -= len_children
        while ptr < 0: ptr += len_children

        popped = children.pop(ptr)

        if popped[1] % 2 == 0: ptr += popped[1] - 1
        else: ptr -= popped[1]
        len_children -= 1
    print(f'Vencedor(a): {children[0][0]}')