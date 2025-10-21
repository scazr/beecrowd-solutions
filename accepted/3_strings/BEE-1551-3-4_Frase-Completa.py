for n in range(int(input())):
    line = set([*input()])
    if ' ' in line: line.remove(' ')
    if ',' in line: line.remove(',')

    if len(line) == 26: print('frase completa')
    elif len(line) >= 13: print('frase quase completa')
    elif len(line) < 13: print('frase mal elaborada')
