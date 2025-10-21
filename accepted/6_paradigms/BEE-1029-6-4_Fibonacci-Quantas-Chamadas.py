def fib_and_calls(n):
    seq = [[None, None] for x in range(n + 1)]
    seq[0], seq[1] = (0, 1) , (1, 1)

    def fib(n):
        
        if seq[n] == [None, None]:
            n1 = fib(n-1)
            n2 = fib(n-2)
            seq[n] = [n1[0] + n2[0], n1[1] + n2[1] + 1]
        return seq[n]

    fib(n)
    return seq[n]

for n in range(int(input())):
    N = int(input())
    OUT = fib_and_calls(N)
    print(f'fib({N}) = {OUT[1] - 1} calls = {OUT[0]}')
    