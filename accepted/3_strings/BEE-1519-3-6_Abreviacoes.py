while True:
    line = input()
    if line[0] == '.': break

    words = line.split()

    abb = dict()

    words_freq = dict()
    for word in words: words_freq[word] = words_freq.setdefault(word, 0) + 1
    words_total = dict()
    for k, v in words_freq.items():
        if len(k) <= 2: words_total[k] = -1
        else: words_total[k] = (len(k) * v) - (2 * v)

    for word in words:
        if words_total[word] != -1:

            abb.setdefault(word[0], word)
            
            if (words_total[word] > words_total[abb[word[0]]]): abb[word[0]] = word

    for ptr_word in range(len(words)):
        word = words[ptr_word]

        if abb.get(word[0]) != None and word == abb[word[0]]: words[ptr_word] = word[0] + '.'
    
    print(' '.join(words))
    print(len(abb))
    for ch in range(26):
        ord_a = ord('a')
        if abb.get(chr(ord_a + ch)) != None: print(f'{chr(ord_a + ch)}. = {abb.get(chr(ord_a + ch))}')
