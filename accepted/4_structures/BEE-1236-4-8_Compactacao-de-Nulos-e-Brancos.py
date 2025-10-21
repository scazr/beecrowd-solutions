import sys

for n in range(int(input())):
    TEXT = input()

    OUT = []

    n_zero, n_space = 0, 0

    for ch in TEXT:
        if ch == '0':
        
            if n_space > 0:
                if n_space > 2: OUT.append('$' + chr(n_space))
                else: OUT.append(' ' * n_space)
                n_space = 0
                
            n_zero += 1
                 
            if n_zero == 255:
                OUT.append('#' + chr(n_zero))
                n_zero = 0             
        
        elif ch == ' ':
            
            if n_zero > 0:
                if n_zero > 2: OUT.append('#' + chr(n_zero))
                else: OUT.append('0' * n_zero)
                n_zero = 0
                
            n_space += 1
                 
            if n_space == 255:
                OUT.append('$' + chr(n_space))
                n_space = 0  
                        
        else:
            if n_zero > 2: OUT.append('#' + chr(n_zero))
            elif n_zero > 0: OUT.append('0' * n_zero)
            
            if n_space > 2: OUT.append('$' + chr(n_space))
            elif n_space > 0: OUT.append(' ' * n_space)
            n_zero, n_space  = 0, 0

            OUT.append(ch)

    if n_zero > 2: OUT.append('#' + chr(n_zero))
    elif n_zero > 0: OUT.append('0' * n_zero)
    
    if n_space > 2: OUT.append('$' + chr(n_space))
    elif n_space > 0: OUT.append(' ' * n_space)
    n_zero, n_space  = 0, 0
    
    sys.stdout.reconfigure(encoding='charmap')
    
    print(''.join(OUT))
