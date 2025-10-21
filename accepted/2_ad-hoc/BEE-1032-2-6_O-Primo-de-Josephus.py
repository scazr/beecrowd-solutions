import math
 
def generatePrime(n):
    primes = []
    X = 0
    i = 2
    prime = False
    while(X < n):
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i%j == 0): prime = False; break
        if prime: X += 1; primes.append(i)
        i += 1
    return primes
     
def josephus(n):
    alive = [_ + 1 for _ in range(n)]
    primes = generatePrime(n - 1)

    index = -1
    for prime in primes:
        index += prime
        while (index >= n): index -= n
        alive.pop(index)
        index -= 1
        n -= 1
    return alive[0]

while True:
    n = int(input())
    if not n: break

    print(josephus(n))
