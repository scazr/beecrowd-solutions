while True:
    try:
        
        string = input()
        line = []
        for i in range(len(string)-1):
            line.append(string[i])
            line.append(' ')
        line.append(string[-1])
        line = ''.join(line)

        white = 0
        for i in range(len(line), 0-1, -2):
            print(' ' * white + line[:i])
            white += 1    
        
        print()

    except EOFError: break