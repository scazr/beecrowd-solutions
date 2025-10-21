from math import gcd

for N in range(int(input())):
    N1 = int(input(), 2)
    N2 = int(input(), 2)

    print('Pair', f'#{N+1}:', 'All you need is love!' if gcd(N1, N2) != 1 else 'Love is not all you need!')
