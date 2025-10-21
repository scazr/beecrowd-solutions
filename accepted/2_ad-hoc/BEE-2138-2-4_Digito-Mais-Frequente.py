from collections import Counter

while True:
    try:
        n = Counter(input()).most_common()
        maxK = None
        maxV = 0
        for k, v in n:
            if v > maxV:
                maxV = v
                maxK = k
            elif v == maxV and (maxK == None or k > maxK):
                maxK = k
        
        print(maxK)

    except EOFError: break