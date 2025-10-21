
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
len_numbers = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3]
I = int(input())
for i in range(I):
    word = input()
    len_word = len(word)

    max_matches = 0
    matched = None
    for n in range(10):
        if len_numbers[n] != len_word: continue

        matches = 0
        for ch in range(len(word)):
            if numbers[n][ch] == word[ch]: matches += 1
        
        if matches > max_matches: matched = n; max_matches = matches

    print(matched)
            