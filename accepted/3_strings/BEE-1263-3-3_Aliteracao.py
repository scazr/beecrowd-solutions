while True:
    try:
        WORDS = input().lower().split()

        last_word = WORDS[0]
        in_alliteration = False
        n_alliteration = 0
        for word in range(1, len(WORDS)):
            word = WORDS[word]

            if word[0] == last_word[0]:
                if not in_alliteration: n_alliteration += 1
                in_alliteration = True 
            else:
                in_alliteration = False
                last_word = word
        
        print(n_alliteration)

    except EOFError:
        break