first = True
while True:
    N = int(input())
    if N == 0: break
    
    if not first: print()
    else: first = False

    names = []
    names_lenght = []
    
    for n in range(N):
        NAME = input()
        names.append(NAME)
        names_lenght.append(len(NAME))
    
    n_spaces = max(names_lenght)
    for ptr_name in range(len(names)):
        print(' ' * (n_spaces - names_lenght[ptr_name]) + names[ptr_name])