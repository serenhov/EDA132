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
    board[x][y] = 'R'
    h = random.randint(0,3)
    h_0 = DIRECTIONS[h]
    print_board(board)
    return x, y, h_0


def current_pos(board):
    for j in range(5):
        for i in range(5):
            if board[i][j] == 'R':
                return i, j
            if board[i][j] == 1:
                return i, j


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
            h = random.randint(0, len(moves)-1)
            move_to = moves[h]
            a = move_to[0]
            b = move_to[1]
            board[a][b] = 'R'
        else:
            a = current[0] + cur_dir[0]
            b = current[1] + cur_dir[1]
            board[a][b] = 'R'
    else:
        moves = find_possible_moves(board, current)
        h = random.randint(0, len(moves)-1)
        move_to = moves[h]
        a = move_to[0]
        b = move_to[1]
        board[a][b] = 'R'
    current = a, b
    return board, current


def robot_walk(board, cur_pos, cur_dir):
    i = 0
    while i < 30:
        board, cur_pos = the_move(board, cur_pos, cur_dir)
     #   print('----- ROBOT WALKING ------')
    #  print_board(board)
        i += 1
        this_board = sensor(cur_pos, board)
        forward_hmm(this_board)


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


def sensor(cur_pos, board):
    print('------ ROBOT: R, SENSOR: AI ------')
    a = 0
    b = 0
    nbh, nbh2 = sensed_possible_moves(cur_pos)
    nbh_l = len(nbh)
    nbh2_l = len(nbh2)
    #p_nothing = 1.0 - 0.1 - nbh_l * 0.05 - nbh2_l * 0.025
    rand = random.randint(1, 1000)
    if rand < 101:
        board[cur_pos[0]][cur_pos[1]] = 1
        print('GOOD JOB')
    elif 101 < rand < 100 + (50 * nbh_l):
        AIpos = random.choice(nbh)
        print(AIpos, "pos")
        board[AIpos[0]][AIpos[1]] = 'AI'
        print('0.05')
        a = AIpos[0]
        b = AIpos[1]
    elif 100 + (50 * nbh_l) < rand < 150 + (25 * nbh2_l):
        AIpos = random.choice(nbh2)
        board[AIpos[0]][AIpos[1]] = 'AI'
        print(AIpos, "pos")
        print('0.025')
        a = AIpos[0]
        b = AIpos[1]
    else:
        print("nothing")
    print('------  ------')
    print_board(board)
    board[a][b] = 0
    return board


def f_matrix():
    f_board = [[1/25 for x in range(5)] for y in range(5)]
    return f_board


def o_matrix(cur_pos):
    sensed_board = [[0 for x in range(5)] for y in range(5)]
    sensed_board[cur_pos[0]][cur_pos[1]] = 0.100
    nbh, nbh2 = sensed_possible_moves(cur_pos)
    for i in nbh:
        sensed_board[i[0]][i[1]] = 0.050
    for i in nbh2:
        sensed_board[i[0]][i[1]] = 0.025
    sensed_board[cur_pos[0]][cur_pos[1]] = 0.100
    return sensed_board


def t_matrix(f_board):
    max_prob = 0
    index = 0
    for i in range(5):
        for j in range(5):
            p = f_board[i][j]
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

'''
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
'''

def forward_hmm(board):
    current = [[]]
    temp = [[0 for x in range(w)] for y in range(h)]
    current = current_pos(board)
    f = f_matrix()
    t = t_matrix(f)
    o = o_matrix(current)
    f = np.dot(f, t)
    f = np.dot(f, o)
    f /= np.sum(f)
    print('------ FORWARD HMM BOARD ------')
    print_board(f)
''' #   alpha = get_alpha(board)
    print('lallla')
    for i in range(5):
        for j in range(5):
            temp[i][j] = t[i][j] * f[j][i]
            f[i][j] = float(o[i][j]) * temp[j][i]
   # a, b = add_T_vec(sensed_board)
   # matrix[a][b] *= 0.7
   '''


w, h = 5, 5;
board = [[0 for x in range(w)] for y in range(h)]
start = start_pos(board)
cur_dir = start[2]
robot_walk(board, start, cur_dir)
