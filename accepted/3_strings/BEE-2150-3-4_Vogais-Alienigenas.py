while True:
    try:
        seq = {*input()}
        phrase = input()
        n = 0
        for ch in phrase:
            if ch in seq: n += 1
        print(n)
    except EOFError: break