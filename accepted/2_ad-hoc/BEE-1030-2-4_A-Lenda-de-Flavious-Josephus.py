for NC in range(int(input())):
    n, k = map(int, input().split())

    ans = 0
    for i in range(1, n+1):
        ans = (ans + k) % i
    
    print(f'Case {NC+1}:', ans + 1)