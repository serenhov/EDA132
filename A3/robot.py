import random
import numpy as np
UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
SENSED_DIRECTIONS = (UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)
UP, DOWN, LEFT, RIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIRECTIONS = (UP, DOWN, LEFT, RIGHT)
WALL, NO_WALL, CORNER = (1, 0, -1)
STATE = (WALL, NO_WALL, CORNER)


def print_board(board):

    print("   1  2  3  4  5")
    i = 1
    for row in board:
        print(i, row)
        i += 1


def start_pos(board):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    print(x, y)
    board[x][y] = 1
    h = random.randint(0,3)
    h_0 = DIRECTIONS[h]
    print_board(board)
    return x, y, h_0


def current_pos(board):
    for j in range(5):
        for i in range(5):
            if board[i][j] == 1:
                cur = i, j
    return cur


def on_board(i):
    return 0 <= i < 5


def find_possible_moves(board, current):
    valid_moves = []
    for d in DIRECTIONS:
        new_row = current[0] + d[0]
        new_column = current[1] + d[1]
        if on_board(new_row) and on_board(new_column):
            valid_moves.append((new_row, new_column))
    return valid_moves


def the_move(board, current, cur_dir):
    board[current[0]][current[1]] = 0
    if on_board(current[0] + cur_dir[0]) and on_board(current[1] + cur_dir[1]):
        r = random.randint(1, 100)
        if r < 31:
            moves = find_possible_moves(board, current)
            print(cur_dir, 'cur_dir')
            h = random.randint(0, len(moves)-1)
            move_to = moves[h]
            a = move_to[0]
            b = move_to[1]
            print(a,'a', b, 'b')
            board[a][b] = 1
        else:
            print(cur_dir, 'cur_dir')
            a = current[0] + cur_dir[0]
            b = current[1] + cur_dir[1]
            print(a,'a', b, 'b')
            board[a][b] = 1
    else:
        print(cur_dir, 'cur_dir')
        moves = find_possible_moves(board, current)
        h = random.randint(0, len(moves)-1)
        move_to = moves[h]
        a = move_to[0]
        b = move_to[1]
        print(a, 'a', b, 'b')
        board[a][b] = 1
    current = a, b
    return board, current


def robot_walk(board, current_pos, cur_dir):
    i = 0
    while i < 5:
        board, current_pos = the_move(board, current_pos, cur_dir)
        print('----- ROBOT WALKING ------')
        print_board(board)
        i += 1
        sensed_board = sensor(current_pos)
    return sensed_board

def sb(new_row, new_column, valid):
    if on_board(new_row) and on_board(new_column):
        if (new_row, new_column) not in valid:
            valid.append((new_row, new_column))
    return valid


def sensed_possible_moves(current):
    valid_moves = []
    valid_moves2 = []
    for d in SENSED_DIRECTIONS:
        new_row = current[0] + d[0]
        new_column = current[1] + d[1]
        valid_moves = sb(new_row, new_column, valid_moves)

    for d in SENSED_DIRECTIONS:
        new_row = current[0] + UP_LEFT[0] + d[0]
        new_column = current[1] + UP_LEFT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sb(new_row, new_column, valid_moves2)
        new_row = current[0] + UP_RIGHT[0] + d[0]
        new_column = current[1] + UP_RIGHT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sb(new_row, new_column, valid_moves2)
        new_row = current[0] + DOWN_LEFT[0] + d[0]
        new_column = current[0] + DOWN_LEFT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sb(new_row, new_column, valid_moves2)
        new_row = current[0] + DOWN_RIGHT[0] + d[0]
        new_column = current[1] + DOWN_RIGHT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sb(new_row, new_column, valid_moves2)
    return valid_moves, valid_moves2



def sensor(cur_pos):
    sensed_board = [[0 for x in range(5)] for y in range(5)]
    sensed_board[cur_pos[0]][cur_pos[1]] = '0.100'
    nbh, nbh2 = sensed_possible_moves(cur_pos)
    for i in nbh:
        sensed_board[i[0]][i[1]] = '0.050'
    for i in nbh2:
        sensed_board[i[0]][i[1]] = '0.025'
    sensed_board[cur_pos[0]][cur_pos[1]] = '0.100'
    print('------ SENSED BOARD ------')
    print_board(sensed_board)
    return sensed_board



def f_matrix():
    f_board = [[1/25 for x in range(5)] for y in range(5)]
    return f_board

def T_matrix(sensed_board):
    max_prob = 0
    index = 0
    for i in range(5):
        for j in range(5):
            p = sensed_board[i][j]
            if p > max_prob:
                max_prob = p
                index = i, j
    t_board = [[0.1 for x in range(5)] for y in range(5)]
    for d in DIRECTIONS:
        if not d == cur_dir:
            t_board[index[0]+d[0]][index[1]+d[1]] = 0.3
        else:
            t_board[index[0]+d[0]][index[1]+d[1]] = 0.7
    return t_board

def get_alpha(sensed_board):
    temp = []
    nbrStates = 16
    alpha = 0;
    max = 0;
    mostLikelyState = -1;
    for row in range(nbrStates):
        temp[row] = 0
        for i in range(nbrStates):
            temp[row] += sensed_board[i][row] * sp[i] * o[row]
    alpha += temp[row]
    alpha = 1 / alpha;
    return alpha


def forward_hmm(sensed_board):
    f = f_matrix()
    T = T_matrix(sensed_board)
    alpha = get_alpha(sensed_board)
    print('lallla')
    for i in range(5):
        for j in range(5):
            f[i][j] = sensed_board[i][j] * T[i][j] * f[i][j]
   # a, b = add_T_vec(sensed_board)
   # matrix[a][b] *= 0.7
    print('------ FORWARD HMM BOARD ------')
    print_board(f)




w, h = 5, 5;
board = [[0 for x in range(w)] for y in range(h)]
start = start_pos(board)
cur_dir = start[2]
sensed_board = robot_walk(board, start, cur_dir)
forward_hmm(sensed_board)