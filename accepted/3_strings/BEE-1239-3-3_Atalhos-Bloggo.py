while True:
    try:
        TEXT = input()
        b = False
        i = False
        trans_text = ''
        for ch in TEXT:
            if ch == '*':
                if not b: trans_text += '<b>'
                else: trans_text += '</b>'
                b = not b
            elif ch == '_':
                if not i: trans_text += '<i>'
                else: trans_text += '</i>'
                i = not i
            else: trans_text += ch
        print(trans_text)
    except EOFError:
        break