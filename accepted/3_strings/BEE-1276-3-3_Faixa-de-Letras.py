ref = "abcdefghijklmnopqrstuvwxyz"
ord_a = ord('a')

while True:
    try:
        TEXT = ''.join(input().split())

        presence = [False for x in range(26)]

        for ch in TEXT: presence[ord(ch) - ord_a] = True
        
        in_range = False
        range_start = None
        range_end = None
        out = []    
        for idx in range(26):
            present = presence[idx]

            if present and not in_range: in_range = True; range_start = idx
            elif not present and in_range: out.append(f'{ref[range_start]}:{ref[idx-1]}'); in_range = False
        if in_range: out.append(f'{ref[range_start]}:{ref[idx]}')
        print(', '.join(out))

    except EOFError:
        break