priority = {'+': 0, '-': 0, '*': 2, '/': 2, '^':3, '(':-1}

for n in range(int(input())):
    INFIX = input()
    

    posfix = []
    op_stack = []

    len_INFIX = len(INFIX)
    for ch in range(len_INFIX):
        ch = INFIX[ch]

        match(ch):
            
            case '+' | '-' | '*' | '/' | '^':

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
