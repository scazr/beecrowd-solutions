N = int(input())
for n in range(N):
    S = int(input())
    sh_height = list(map(int, input().split()))
    action = [*input()]

    hit = 0
    for turn in range(S):
        if action[turn] == 'J' and sh_height[turn] > 2: hit += 1
        elif action[turn] == 'S' and 0 < sh_height[turn] <= 2: hit += 1

    print(hit)