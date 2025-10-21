while True:
    try:
        swap = {
            '@':'a',
            '&': 'e',
            '!': 'i',
            '*': 'o',
            '#': 'u',
        }

        print(''.join(map(lambda x : swap.get(x) if swap.get(x) != None else x, input())))
    
    except EOFError: break