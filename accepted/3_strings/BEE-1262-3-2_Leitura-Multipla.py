while True:
    try:
        TRACE = input()
        PROCS = int(input())
        
        cycles = 0
        read_count = 0
        for trace in TRACE:
            if trace == 'W': cycles += 2 if read_count > 0 else 1; read_count = 0
            elif trace == 'R':
                read_count += 1
                if read_count == PROCS:
                    cycles += 1
                    read_count = 0
        if read_count > 0: cycles += 1
        print(cycles)

    except EOFError:
        break