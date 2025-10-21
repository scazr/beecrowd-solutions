for n in range(int(input())):
    N_STUD = int(input())
    NAMES = input().split()
    ATT = input().split()

    underatt = []
    for ptr_stud in range(N_STUD):
        att = 0
        counted_classes = len(ATT[ptr_stud])
        for day in ATT[ptr_stud]:
            if day == 'P': att += 1
            elif day == 'M': counted_classes -= 1
        if att*100/counted_classes < 75: underatt.append(NAMES[ptr_stud])

    print(' '.join(underatt))