while True:
    try:
        STR1 = input()
        STR2 = input()

        m = len(STR1)
        n = len(STR2)

        LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

        result = 0

        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    LCSuff[i][j] = 0
                elif (STR1[i-1] == STR2[j-1]):
                    LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                    result = max(result, LCSuff[i][j])
                else:
                    LCSuff[i][j] = 0

        print(result)
    except EOFError: break


         