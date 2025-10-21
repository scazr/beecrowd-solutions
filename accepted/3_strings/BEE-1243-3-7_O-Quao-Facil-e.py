while True:
    try:
        PROBLEM = input().split()

        valid_words = []
        
        for prob in PROBLEM:
            valid = True
            len_prob = len(prob)
            for ch in range(len_prob - 1):
                ord_ch = ord(prob[ch])
                if not (ord_ch >= 65): valid = False; break
            ord_ch = ord(prob[-1])
            if valid and (ord_ch == 46 or ord_ch >= 65):
                if ord_ch == 46: valid_words.append(len_prob - 1)
                else: valid_words.append(len_prob)
        
        len_valid_words = len(valid_words)
        if len_valid_words != 0: average = sum(valid_words) // len(valid_words)
        else: average = 0

        print(250 if average <= 3 else 500 if 3 < average and average < 6 else 1000)
        
    except EOFError:
        break