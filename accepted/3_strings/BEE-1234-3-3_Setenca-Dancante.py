try:
    while True:
        TEXT = input()
        captalize = True
        for char in TEXT:
            if char == ' ': print(' ', end=''); continue
            print(char.capitalize() if captalize else char.lower(), end='')
            captalize = not captalize
        print()
except EOFError:
    pass