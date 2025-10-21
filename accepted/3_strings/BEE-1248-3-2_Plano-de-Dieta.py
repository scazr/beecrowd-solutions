for n in range(int(input())):
    DIET = [*input()]
    BREAK = [*input()]
    LUNCH = [*input()]

    diet_keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    diet = [0 for x in range(26)]
    hash = ord('A')
    cheater = False
    for food in DIET: diet[ord(food) - hash] += 1
    
    for food in BREAK:
        if diet[ord(food) - hash] == 0: cheater = True; break
        diet[ord(food) - hash] -= 1
    
    if not cheater:
        for food in LUNCH:
            if diet[ord(food) - hash] == 0: cheater = True; break
            diet[ord(food) - hash] -= 1
    
    if not cheater:
        for food in range(26): print(diet_keys[food] * diet[food], end='')
        print()
    else: print('CHEATER')