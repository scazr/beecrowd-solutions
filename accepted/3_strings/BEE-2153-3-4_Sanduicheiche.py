while True:
    try:
        word = input()[::-1]
        for i in range(1, (len(word)//2)+1):
            
            if word[:i] == word[i:i+i]:
                print(word[i:][::-1])
                break
        else:
            print(word[::-1])

    except EOFError: break