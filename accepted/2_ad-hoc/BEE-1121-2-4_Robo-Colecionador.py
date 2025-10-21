while True:
    N, M, S = map(int, input().split())
    if N == 0 and M == 0 and S == 0: break

    grid = []
    facing = None
    position = None
    for n_pos in range(N):
        line = [*input()]
        grid.append(line)

        if   'N' in line: m_pos = line.index('N')
        elif 'S' in line: m_pos = line.index('S')
        elif 'L' in line: m_pos = line.index('L')
        elif 'O' in line: m_pos = line.index('O')
        else: continue
                
        facing = line[m_pos]
        position = [n_pos, m_pos]
        
    n_sticker = 0

    def pos_eval(n, m):
        global n_sticker

        n_pos = position[0] + n
        m_pos = position[1] + m
    
        if n_pos < 0 or n_pos >= N or m_pos < 0 or m_pos >= M: return

        cell = grid[n_pos][m_pos]
        
        if cell == '*': n_sticker += 1; grid[n_pos][m_pos] = '.'
        elif cell == '#': return
        
        position[0] += n
        position[1] += m
    
    instructions = input()
    for instruction in instructions:
        match(instruction):
            case 'F':
                match(facing):
                    case 'N': pos_eval(-1, 0)
                    case 'S': pos_eval(1, 0)
                    case 'L': pos_eval(0, 1)
                    case 'O': pos_eval(0, -1)
            case 'E':
                match(facing):
                    case 'N': facing = 'O'
                    case 'O': facing = 'S'
                    case 'S': facing = 'L'
                    case 'L': facing = 'N'
            case 'D':
                match(facing):
                    case 'N': facing = 'L'
                    case 'L': facing = 'S'
                    case 'S': facing = 'O'
                    case 'O': facing = 'N'

    print(n_sticker)