test = 1
while True:
    board = [[1 for x in range(8)] for x in range(8)]

    KNIGHT = input()
    knight_pos = int(KNIGHT[0]) - 1, ord(KNIGHT[-1]) - ord('a')
    if int(KNIGHT[0]) == 0: break

    for p in range(8):
        PAWN = input()
        pawn_pos = int(PAWN[0]) - 1, ord(PAWN[1]) - ord('a')

        if pawn_pos[0] != 0:
            if pawn_pos[1] != 0: board[pawn_pos[0] - 1][pawn_pos[1] - 1] = 0
            if pawn_pos[1] != 7: board[pawn_pos[0] - 1][pawn_pos[1] + 1] = 0

    moves = 0
    if knight_pos[0] >= 2:
        if knight_pos[1] >= 1 and board[knight_pos[0] - 2][knight_pos[1] - 1]: moves += 1
        if knight_pos[1] <= 6 and board[knight_pos[0] - 2][knight_pos[1] + 1]: moves += 1
    if knight_pos[0] <= 5:
        if knight_pos[1] >= 1 and board[knight_pos[0] + 2][knight_pos[1] - 1]: moves += 1
        if knight_pos[1] <= 6 and board[knight_pos[0] + 2][knight_pos[1] + 1]: moves += 1
    if knight_pos[1] >= 2:
        if knight_pos[0] >= 1 and board[knight_pos[0] - 1][knight_pos[1] - 2]: moves += 1
        if knight_pos[0] <= 6 and board[knight_pos[0] + 1][knight_pos[1] - 2]: moves += 1
    if knight_pos[1] <= 5:
        if knight_pos[0] >= 1 and board[knight_pos[0] - 1][knight_pos[1] + 2]: moves += 1
        if knight_pos[0] <= 6 and board[knight_pos[0] + 1][knight_pos[1] + 2]: moves += 1

    print(f'Caso de Teste #{test}:', moves, 'movimento(s).')
    
    test += 1

