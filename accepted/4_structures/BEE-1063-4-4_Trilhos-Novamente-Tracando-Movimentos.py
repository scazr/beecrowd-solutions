while True:
    N = int(input())
    if N == 0: break

    IN = list(input().split())
    OUT = list(input().split())

    ptr_IN = 0
    ptr_OUT = 0

    stack = [0]
    result = []
    possible = True

    while ptr_OUT < N:
        if ptr_IN < N and IN[ptr_IN] == OUT[ptr_OUT]: result.append('I'); result.append('R'); ptr_IN += 1; ptr_OUT += 1; #rint('a')
        elif stack[-1] != 0 and stack[-1] == OUT[ptr_OUT]: stack.pop(-1); result.append('R'); ptr_OUT += 1; #print('b')
        elif ptr_IN < N: result.append('I'); stack.append(IN[ptr_IN]); ptr_IN += 1; #print('c')
        else: possible = False; break
    print(''.join(result), end='')
    if not possible: print(' Impossible', end='')
    print()