N = int(input())

strings = []

for _ in range(N):
    strings.append(input().split())

for string in strings:
    string = " ".join(sorted(string, key=lambda word: len(word),reverse=True))
    print(string)
