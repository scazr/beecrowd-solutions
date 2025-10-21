C = int(input())
for c in range(C):
    N = int(input())
    words = set()
    for n in range(N):
        word, action = input().split()
        if action == 'chirrin': words.add(word)
        elif action == 'chirrion' and word in words: words.remove(word)
    
    print('TOTAL')
    for w in sorted(list(words)):
        print(w)
        