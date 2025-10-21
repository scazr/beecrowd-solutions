letters = 'abcdefghijklmnopqrstuvwxyz'

ord_a = ord('a')
ord_z = ord('z')

for n in range(int(input())):
    TEXT = input().lower()
    
    frequency = [[letters[x], 0] for x in range(len(letters))]

    for ch in TEXT:
        ord_ch = ord(ch)
        if ord_a <= ord_ch and ord_ch <= ord_z:
            frequency[ord_ch - ord_a][1] += 1
    
    frequency = sorted(frequency, key=lambda ch : (ch[1], not ch[0]), reverse=True)
    
    largest = frequency[0][1]
    for _ in range(26):
        if frequency[_][1] != largest: break
        print(frequency[_][0], end='')
    print()
        