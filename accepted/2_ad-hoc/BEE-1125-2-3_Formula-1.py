while True:
    G, P = map(int, input().split())
    if G == 0 or P == 0: break

    races = []
    for g in range(G):
        Q = tuple(map(int, input().split()))
        races.append(Q)

    S = int(input())
    for s in range(S):
        scores = [0 for x in range(P)]
        S_input = tuple(map(int, input().split()))
        K = S_input[0]
        k = S_input[1:]

        for race in races:
            for pilot in range(P):
                if race[pilot] > K: continue
                scores[pilot] += k[race[pilot] - 1]

        max_score = max(scores)
        winners = []
        for racer in range(P):
            if scores[racer] == max_score: winners.append(racer+1)
        print(*winners)
