N = []
for case in range(0, int(input())):
    M = [*input()]
    for letter in range(0, len(M)):
        if (ord("A") <= ord(M[letter]) and ord(M[letter]) <= ord("Z")) or (ord("a") <= ord(M[letter]) and ord(M[letter]) <= ord("z")):
            M[letter] = chr(ord(M[letter]) + 3)
    M.reverse()
    for letter in range(int(len(M)/2), len(M)):
        M[letter] = chr(ord(M[letter]) - 1)
    M = "".join(M)
    N.append(str(M))

for answer in N:
    print(answer)
