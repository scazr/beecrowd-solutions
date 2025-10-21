while True:
    WORDS = input().split()
    if WORDS[0] == '*': break

    letter = WORDS[0][0].lower()
    tautogram = True
    for word in WORDS:
        if word[0].lower() != letter: tautogram = False
    print('Y' if tautogram else 'N')