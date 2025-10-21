import sys
first = True
min_ord = 33
while True:
    try:
        freq = [[n + min_ord, 0] for n in range(96)]
        
        LINE = input().replace(' ', '')
        for ch in LINE:
            freq[ord(ch) - min_ord][1] += 1
        
        freq = sorted(freq, key = lambda x : (x[1], -x[0]))

        if not first: print()
        else: first = False
        
        for ch in range(96 - 1, -1, -1):
            if freq[ch][1] == 0:
                for ch in range(ch + 1, 96):
                    print(freq[ch][0], freq[ch][1])
                break

    except EOFError: break