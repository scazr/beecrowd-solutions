for n in range(int(input())):
    CIPHER = input()
    ROT = int(input())
    
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hash = ord('A')

    decode = ''
    for ch in CIPHER: decode += key[ord(ch) - hash - ROT]
    print(decode)