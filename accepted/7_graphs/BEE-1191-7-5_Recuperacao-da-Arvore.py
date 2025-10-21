def post_conversion(pre_ord, in_ord):
    pos_ord = []
    ptr_pre = 0
    
    def post_conv(string:str):
        nonlocal ptr_pre
        
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
    
    post_conv(in_ord)

    return ''.join(pos_ord)

while True:
    try:
        pre_ord, in_ord = input().split()
        
        print(post_conversion(pre_ord, in_ord))
        
    except: break