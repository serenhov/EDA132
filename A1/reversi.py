
from pip._vendor.distlib.compat import raw_input

UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, 1), (1, -1), (1, 1)]
DIRECTIONS = (UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)
EMPTY, BLACK, WHITE, OUTER = 'X', 1, -1, '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = (BLACK, WHITE)



w, h = 8, 8;
board = [[0 for x in range(w)] for y in range(h)]
board[3][3] = BLACK
board[4][4] = BLACK
board[4][3] = WHITE
board[3][4] = WHITE
for row in board:
    print(row)


def find_possible_moves(board, player):
    valid_moves = []
    for j in range(8):
        for i in range(8):
            moves = 0
            if board[i][j] == player:
                #print(i, j, "location for player")
                for d in DIRECTIONS:
                    new_row = i + d[0]
                    new_column = j + d[1]
                   # print(new_row, new_column)
                    if board[new_row][new_column] == -player:
                        moves = 1
                        new_row += d[0]
                        new_column += d[1]
                       # print(new_row, new_column, "hej")
                        if board[new_row][new_column] == 0 and moves == 1:
                            valid_moves.append((new_row, new_column))
    return print(valid_moves)
#find_possible_moves(board, 1)

def make_move(board, player, row, column):
    #if (row, column) not in find_possible_moves(board, player):
     #   return 0
    board[row][column] = player
    flip(board, player, row, column)
    return 1


def flip(board, player, row, column):
    flips = []
    for d in DIRECTIONS:
        new_row = row + d[0]
        new_column = column + d[1]
        while board[new_row][new_column] == -player:
            flips.append((new_row, new_column))
            print(flips, "flip listan")
            new_row += d[0]
            new_column += d[1]
            print(board[new_row][new_column], "värdet på playts 33")
            if board[new_row][new_column] == player:
                i = 0
                for f in flips:
                    print("flip")
                    a = flips[i][0]
                    b = flips[i][1]
                    print("a =", a, "b =", b)
                    board[a][b] = player
                    i += 1
    for row in board:
        print(row)

make_move(board, 1, 5, 3)


def calculate_points(board, player):
    count = 0
    for j in range(8):
        for i in range(8):
            if board[i][j] == player:
                count += 1
    return print(count)

calculate_points(board,1)

def calculate_winner(board):
    white = 0
    black = 0
    for j in range(8):
        for i in range(8):
            if board[i][j] == WHITE:
                white += 1
            elif board[i][j] == BLACK:
                black += 1
    if black > white:
        return print('black won.')
    elif black == white:
        return print('equal.')
    else:
        return print('white won')
calculate_winner(board)

def mini_max(alpha, beta, board, player, time_limit, depth):
    if depth == 0 or find_possible_moves(board,player).len() == 0:
        return calculate_points(board, player)
    if time_limit <= 0:
        return calculate_points(board, player)
    if player == 1:
        for move in find_possible_moves(board, player):
            alpha = max(alpha, mini_max(alpha, beta, board, -player, depth-1))
            if alpha >= beta:
                break
    elif player == -1:
        for move in find_possible_moves(board,player):
            beta = min(beta, mini_max(alpha, beta, board, -player, depth-1))
            if alpha >= beta:
                break






