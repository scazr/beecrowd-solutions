first = True
i = 1
while True:
    a = input()
    if a == '0': break
    
    if first: first = False
    else: print()
    
    n = input()
    print('Instancia', i)
    print('verdadeira' if n.find(a) != -1 else 'falsa')
    i += 1