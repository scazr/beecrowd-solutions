def sumDigit(n):
    total = 0
    while n >= 1:
        total += n % 10
        n //= 10
    return total

while True:
    N, M = input().split()
    if N == M == '0': break
    
    n, m = int(N), int(M)
    
    while n >= 10: n = sumDigit(n)
    while m >= 10: m = sumDigit(m)
    
    if n > m: print(1)
    elif n == m: print(0)
    elif n < m: print(2)


