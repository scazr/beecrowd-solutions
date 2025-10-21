while True:
    try:
        N = int(input())

        NUMBERS = []
        for n in range(N): NUMBERS.append(input())
        NUMBERS = list(sorted(NUMBERS))

        prev_ph, ph = None, NUMBERS[0]
        max_ptr = len(ph) - 1
        ptr = -1
        ch_saved = 0

        for n in range(1, N):
            prev_ph, ph = ph, NUMBERS[n]
            
            for ptr_check in range(ptr + 1):
                if prev_ph[ptr_check] != ph[ptr_check]: ptr = ptr_check - 1; break

            if ptr < max_ptr and prev_ph[ptr + 1] == ph[ptr + 1]:
                while ptr < max_ptr and prev_ph[ptr + 1] == ph[ptr + 1]:
                    ptr += 1
            
            ch_saved += ptr + 1
        
        print(ch_saved)
            
    except EOFError: break