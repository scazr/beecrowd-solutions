N = int(input())

for n in range(N):
    chs = [*input()]
    chs[0] = int(chs[0])
    chs[2] = int(chs[2])

    if chs[0] == chs[2]: print(chs[0] * chs[2])
    elif chs[1].islower(): print(chs[0] + chs[2])
    else: print(chs[2] - chs[0])