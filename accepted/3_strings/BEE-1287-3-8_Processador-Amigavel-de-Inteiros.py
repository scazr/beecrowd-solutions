while True:
    INT_MAX = (2**31) - 1
    try:
        n = ''.join(list(map(lambda x : '0' if x == 'o' or x == 'O' else '1' if x == 'l' else x, input()))).replace(',', '').replace(' ', '')

        try:
            n = int(n)
            if n > INT_MAX: raise Exception
            print(n)
        except:
            print('error')

    except EOFError: break