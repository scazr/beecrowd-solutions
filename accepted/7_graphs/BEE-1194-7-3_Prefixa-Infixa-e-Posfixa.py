def post_conv(string:str):
    global ptr_pre
    
    if string == '': ptr_pre -= 1; return ''
    elif len(string) == 1:
        return string
    
    ptr_mid = string.find(pre_ord[ptr_pre])
    lsubstr = string[:ptr_mid]
    rsubstr = string[ptr_mid+1:]

    ptr_pre += 1
    pos_ord.append(post_conv(lsubstr))
    
    ptr_pre += 1
    pos_ord.append(post_conv(rsubstr))

    pos_ord.append(string[ptr_mid])

    return ''
    

C = int(input())
for c in range(C):
    N, pre_ord, in_ord = input().split()
    N = int(N)

    pos_ord = []
    ptr_pre = 0
    post_conv(in_ord)
    print(''.join(pos_ord))
