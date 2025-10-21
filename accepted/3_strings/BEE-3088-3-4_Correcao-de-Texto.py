while True:
    try:
        string = input()
        print(string.replace(' ,', ',').replace(' .', '.'))
    except EOFError: break