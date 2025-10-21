for n in range(int(input())):
    TEXT = input()
    len_text = len(TEXT)
    for ch in reversed(range(int(len_text/2))):
        print(TEXT[ch], end='')
    for ch in reversed(range(int(len_text/2), len_text)):
        print(TEXT[ch], end='')
    print()