N = int(input())

freq = dict()

for n in range(N):
    num = int(input())
    freq.setdefault(num, 0)
    freq[num] += 1

for k in sorted(freq):
    print(k, 'aparece', freq[k], 'vez(es)')
