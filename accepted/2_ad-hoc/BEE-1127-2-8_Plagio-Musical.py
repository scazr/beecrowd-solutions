swap_reference = {
    'A': 'b',
    'b': 'B',
    'B': 'C',
    'C': 'd',
    'd': 'D',
    'D': 'e',
    'e': 'E',
    'E': 'F',
    'F': 'g',
    'g': 'G',
    'G': 'a',
    'a': 'A'
    }
normalize_reference = {
                'A'  : 'A',
                'A#' : 'b',
                'Bb' : 'b',
                'B'  : 'B',
                'Cb' : 'B',
                'B#' : 'C',
                'C'  : 'C',
                'C#' : 'd',
                'Db' : 'd',
                'D'  : 'D',
                'D#' : 'e',
                'Eb' : 'e',
                'E'  : 'E',
                'Fb' : 'E',
                'E#' : 'F',
                'F'  : 'F',
                'F#' : 'g',
                'Gb' : 'g',
                'G'  : 'G',
                'G#' : 'a',
                'Ab' : 'a'
                }


def normalize(fragment: str) -> str:
        normalized = []
        for note in fragment:
            normalized.append(normalize_reference[note])
            
        return ''.join(normalized)

def rot_key(key) -> str:
    new_key = []
    for note in key:
        new_key.append(swap_reference[note])
    return ''.join(new_key)

def KMP(haystack: str, needle: str) -> int:
    if needle == '': return 0
    lps = [0] * len(needle)

    prev_lps, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prev_lps]:
            lps[i] = prev_lps + 1
            prev_lps += 1
            i += 1
        elif prev_lps == 0:
            lps[i] = 0
            i += 1
        else:
            prev_lps = lps[prev_lps - 1]

    i = 0
    j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]: i, j = i + 1, j + 1
        else:
            if j == 0: i += 1
            else: j = lps[j - 1]   
        if j == len(needle): return i - len(needle)
    
    return -1

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)

    last_occurrence = {pattern[i]: i for i in range(m)}
    i = m - 1
    j = m - 1

    while i < n:
        if pattern[j] == text[i]:
            if j == 0: return i
            i -= 1
            j -= 1
        else:
            i += m - min(j, 1 + last_occurrence.get(text[i], -1))
            j = m - 1

    return -1 

while True:
    M, T = map(int, input().split())
    if M == 0 and T == 0: break

    SONG = input().split()
    SUSPECT = input().split()

    song = normalize(SONG)
    suspect_key = normalize(SUSPECT)

    found = False
    if boyer_moore_search(song, suspect_key) >= 0: found = True
    else:
        for key in range(11):
            suspect_key = rot_key(suspect_key)
            if boyer_moore_search(song, suspect_key) >= 0: found = True; break
    print('S' if found else 'N')
