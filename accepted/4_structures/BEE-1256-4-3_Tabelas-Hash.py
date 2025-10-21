for case in range(int(input())):
    if case != 0: print("")
    M, C = map(int, input().split())
    CKeys = tuple(map(int, input().split()))
    hashTable = [[] for _ in range(M)] 
    for key in CKeys: hashTable[key % M].append(key)
    for keys in range(len(hashTable)): 
        print(keys, *hashTable[keys], sep=" -> ", end=" -> \\\n")