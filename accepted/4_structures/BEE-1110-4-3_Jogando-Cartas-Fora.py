while True:
    INPUT = int(input())
    if INPUT == 0: break
    deck = [x for x in range(1, INPUT + 1)]
    tempDeck = deck.copy()
    discarded = []
    while len(tempDeck) > 1:
        for _ in tempDeck:
            if tempDeck.index(_) % 2 == 0: discarded.append(_); deck.remove(_); deck.append(deck.pop(0))

        tempDeck = deck.copy()
        
    print("Discarded cards: ", end=""); print(*discarded, sep=", ")
    print("Remaining card:", *deck) 
