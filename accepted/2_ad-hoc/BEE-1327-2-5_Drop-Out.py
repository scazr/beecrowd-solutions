while True:
    N = int(input())
    if N == 0: break

    NAMES = input().split()
    DECK = []
    for _ in range(4):
        LINE = map(int, input().split())
        DECK += LINE
    
    len_names = len(NAMES)
    len_deck = len(DECK)
    eliminated = []
    while len_names:

        if len_names > len_deck: eliminated = NAMES[::-1]; break

        min_round_card = min(DECK[:len_names])

        eliminated = []
        popped_names = 0
        for idx in range(len_names -1, -1, -1):
            if DECK[idx] == min_round_card:
                eliminated.append(NAMES.pop(idx))
                popped_names += 1
        
        for _ in range(len_names): DECK.pop(0)
        
        len_deck -= len_names
        len_names -= popped_names

    print(' '.join(eliminated[::-1]) + ' ')