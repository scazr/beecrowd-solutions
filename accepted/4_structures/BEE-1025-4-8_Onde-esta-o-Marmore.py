cases = 0
while True:
    cases += 1
    N, Q = map(int, input().split())
    if not N and not Q: break
    marbles, guesses = [], []
    for _ in range(N): marbles.append(int(input()))
    for _ in range(Q): guesses.append(int(input()))

    marbles = sorted(marbles)

    print("CASE# {0}:".format(cases))
    for guess in guesses:

        high, mid, low = len(marbles), None, 0
        last, found = None, False
    
        while True:
            mid = int((high + low)/2)
            if mid == last: break

            if marbles[mid] < guess: low = mid;
            elif marbles[mid] > guess: high = mid;
            elif marbles[mid] == guess: found = True; break;

            last = mid
            
        if not found: print("{0} not found".format(guess))
        if found:
            while marbles[mid] == marbles[mid - 1]: mid -= 1
            print("{0} found at {1}".format(guess, mid + 1));
