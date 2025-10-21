ORD_A = ord('A')

for n in range(int(input())):
    total_hash = 0
    
    for l in range(int(input())):
        STR = input()
        
        line_hash = 0
        for ptr_ch in range(len(STR)): line_hash += ord(STR[ptr_ch]) - ORD_A + l + ptr_ch
        
        total_hash += line_hash
    
    print(total_hash)