while True:
    try: print('Y' if int(input()) % 6 == 0 else 'N')
    except EOFError: break