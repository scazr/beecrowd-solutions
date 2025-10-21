first = True
while True:
    N = int(input())
    if N == 0: break

    if not first: print()
    else: first = False
    
    PERM_LIST = []
    
    while True:
        PERM = list(map(int,input().split()))
        if PERM[0] == 0: break
        PERM_LIST.append(PERM)
    

    for PERM in PERM_LIST:
        next_coach = N
        stack = [N + 1]

        ptr_coach = N - 1
        while ptr_coach >= 0:
            coach = PERM[ptr_coach]

            if coach == next_coach: PERM.pop(-1); next_coach -= 1
            elif stack[-1] == next_coach: stack.pop(-1); next_coach -= 1; ptr_coach += 1
            else: stack.append(PERM.pop(-1))
            
            ptr_coach -= 1

        while True:
            if stack[-1] == next_coach: stack.pop(-1); next_coach -= 1
            else: break
        
        if len(stack) > 1: print('No')
        else: print('Yes')
print()