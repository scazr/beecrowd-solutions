priority = {
    '^':6,
    '*': 5, '/': 5,
    '+': 4, '-': 4,
    '>': 3, '<': 3, '=': 3, '#': 3,
    '.': 2,
    '|': 1,
    '(': -1
            }    

ord_A = ord('A')
ord_Z = ord('Z')
ord_a = ord('a')
ord_z = ord('z')
ord_1 = ord('0')
ord_9 = ord('9')

def validation(EXP: str, len_EXP: int):
    par_level = 0
    must_op = False
    
    first = True
    for ch in range(len_EXP):
        ch = EXP[ch]
        ord_ch = ord(ch)

        if ((ord_A <= ord_ch and ord_ch <= ord_Z) or
            (ord_a <= ord_ch and ord_ch <= ord_z) or
            ord_1 <= ord_ch and ord_ch <= ord_9):
            if must_op: return False, 1
            must_op = True

        elif (ch in priority and priority[ch] != -1): 
            if not must_op: return False, 1
            must_op = False
        
        elif (ord_ch == ord('(')):
            if not first and must_op: return False, 1
            must_op = False
            par_level += 1 
        elif (ord_ch == ord(')')):
            if not must_op: return False, 0
            must_op = True
            par_level -= 1

        else: return False, 0
    
    if not must_op: return False, 1
    elif par_level != 0: return False, 1
    
    first = False

    return True, None

while True:
    try:
        EXP = input()

        posfix = []
        op_stack = []

        len_INFIX = len(EXP)

        a = validation(EXP, len_INFIX)
        if not a[0]:
            if a[1] == 0: print('Lexical Error!')
            else: print('Syntax Error!')
            continue

        for ch in range(len_INFIX):
            ch = EXP[ch]

            match(ch):
                case '+' | '-' | '*' | '/' | '^' | '>' | '<' | '=' | '#' | '.' | '|':
                    while op_stack and (priority[ch] < priority[op_stack[-1]] or
                    (priority[ch] == priority[op_stack[-1]] and ch != '^')):
                        posfix.append(op_stack.pop())
                    op_stack.append(ch)

                case '(': op_stack.append(ch)
                
                case ')':
                    while op_stack and op_stack[-1] != '(':
                        posfix.append(op_stack.pop())
                    op_stack.pop()
                case _:
                    posfix.append(ch)

        while op_stack: posfix.append(op_stack.pop(-1))
        print(''.join(posfix))

    except EOFError: break