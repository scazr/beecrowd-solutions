OUTPUT = []
for N in range(int(input())):
    mine = input()

    parenthesis = 0
    diamond = 0
    for _ in mine:
        if _ == "<": parenthesis += 1
        elif _ == ">" and parenthesis > 0: diamond += 1; parenthesis -= 1
        
    OUTPUT.append(diamond)

for _ in OUTPUT: print(_)
