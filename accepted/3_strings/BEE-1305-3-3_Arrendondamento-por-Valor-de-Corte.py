while True:
    try:
        num = float(input())
        cutoff = float(input())
        dec = num - int(num)
        if dec >= cutoff: print(int(num) + 1)
        else: print(int(num))
    except EOFError: break