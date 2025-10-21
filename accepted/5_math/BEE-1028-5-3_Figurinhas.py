OUTPUT = []
for N in range(int(input())):
    F1, F2 = map(int, input().split())

    F1, F2 = max(F1, F2), min(F1, F2)
    
    while F2 != 0: F1, F2 = F2, F1 % F2
    OUTPUT.append(F1)

for _ in OUTPUT: print(_)