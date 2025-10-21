for n in range(int(input())):
    str1, str2 = input().split()

    max_str = max(str1, str2, key=len)
    min_len = min(len(str1), len(str2))
    for ch in range(min_len):
        print(str1[ch] + str2[ch], end='')
    print(max_str[min_len:])
