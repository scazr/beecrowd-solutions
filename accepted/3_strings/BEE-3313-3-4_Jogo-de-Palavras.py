from itertools import count
from collections import deque

for i in count(1):
    string = input()
    minStr = None
    maxStr = None
    if string == '*': break

    deqString = deque(string)
    rotations = [deqString.copy() for n in range(len(string))]
    for nRotations in range(0, len(string)):
        rotations[nRotations].rotate(nRotations)

    print(f'Caso {i}:', ''.join(list(min(rotations))), ''.join(list(max(rotations))))