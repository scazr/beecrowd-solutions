def main():
    sBiggest = None
    nBiggest = 0

    while True:
        STRING = input()
        if STRING == '0': break

        STRING = STRING.split()
        lenWords = []
        for word in STRING:
            lenWords.append(str(len(word)))
            if len(word) >= nBiggest:
                nBiggest, sBiggest = len(word), word
        
        print('-'.join(lenWords))

    print()
    print('The biggest word:', sBiggest)

main()