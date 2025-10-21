import re
words = set()
while True:
    try:
        pattern = re.compile('[^A-Za-z\s]')
        TEXT = re.sub(pattern, ' ', input().lower()).split()
        for word in TEXT: words.add(word)
        
    except EOFError: break
OUT = sorted(words)
for word in OUT: print(word)