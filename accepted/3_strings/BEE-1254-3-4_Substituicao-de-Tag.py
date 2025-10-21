import re
while True:
    try:
        ORG_TAG = input()
        SUBS = input()
        TEXT = input()

        len_text = len(TEXT)

        split_text = []
        ptr_last_split = 0
        in_tag = False
        out_tag_text = ''
        for ptr_ch in range(len_text):
            char = TEXT[ptr_ch]
            if char == '<':
                if ptr_ch - ptr_last_split != 0: split_text.append(TEXT[ptr_last_split : ptr_ch])
                in_tag = True
                ptr_last_split = ptr_ch 
            elif char == '>':
                if ptr_ch - ptr_last_split != 0: split_text.append(TEXT[ptr_last_split : ptr_ch+1])
                in_tag = False
                ptr_last_split = ptr_ch + 1
        if ptr_last_split != len_text: split_text.append(TEXT[ptr_last_split :])

        for ptr_text in range(len(split_text)):
            if split_text[ptr_text][0] == '<':
                pattern = re.compile(ORG_TAG, re.IGNORECASE)
                split_text[ptr_text] = pattern.sub(SUBS, split_text[ptr_text])
                
        print(''.join(split_text))
    except EOFError:
        break