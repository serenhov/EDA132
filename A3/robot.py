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

# Random start position for the robot
def start_pos(board):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    board[x][y] = 'R'
    h = random.randint(0,3)
    h_0 = DIRECTIONS[h]
    print_board(board)
    return x, y, h_0


# Returns current position for the robot
def current_pos(board):
    for j in range(5):
        for i in range(5):
            if board[i][j] == 'R':
                return i, j
            if board[i][j] == 1:
                return i, j


# Checks if the position is within the board
def on_board(i):
    return 0 <= i < 5


def on_f_board(i):
    return 0 <= i < 100


# Possible moves for the robot
def find_possible_moves(board, current):
    valid_moves = []
    for d in DIRECTIONS:
        new_row = current[0] + d[0]
        new_column = current[1] + d[1]
        if on_board(new_row) and on_board(new_column):
            valid_moves.append((new_row, new_column))
    return valid_moves


# Returns the new position of the robot
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


# Robot walks x times
def robot_walk(board, cur_pos, cur_dir):
    i = 0
    while i < 1000:
        board, cur_pos = the_move(board, cur_pos, cur_dir)
        i += 1
        this_board = sensor(cur_pos, board)
        forward_hmm(this_board)


# Help function for possible states for the sensor
def sensor_on_board(new_row, new_column, valid):
    if on_board(new_row) and on_board(new_column):
        if (new_row, new_column) not in valid:
            valid.append((new_row, new_column))
    return valid


# Possible states for the sensor
def sensed_possible_states(current):
    valid_moves = []
    valid_moves2 = []
    for d in SENSED_DIRECTIONS:
        new_row = current[0] + d[0]
        new_column = current[1] + d[1]
        valid_moves = sensor_on_board(new_row, new_column, valid_moves)
    for d in SENSED_DIRECTIONS:
        new_row = current[0] + UP_LEFT[0] + d[0]
        new_column = current[1] + UP_LEFT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sensor_on_board(new_row, new_column, valid_moves2)
        new_row = current[0] + UP_RIGHT[0] + d[0]
        new_column = current[1] + UP_RIGHT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sensor_on_board(new_row, new_column, valid_moves2)
        new_row = current[0] + DOWN_LEFT[0] + d[0]
        new_column = current[0] + DOWN_LEFT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sensor_on_board(new_row, new_column, valid_moves2)
        new_row = current[0] + DOWN_RIGHT[0] + d[0]
        new_column = current[1] + DOWN_RIGHT[1] + d[1]
        if (new_row, new_column) not in valid_moves:
            valid_moves2 = sensor_on_board(new_row, new_column, valid_moves2)
    return valid_moves, valid_moves2


# Sensor, returns position of the sensor
def sensor(cur_pos, board):
    print('------ ROBOT: R, SENSOR: AI ------')
    a = 0
    b = 0
    nbh, nbh2 = sensed_possible_states(cur_pos)
    nbh_l = len(nbh)
    nbh2_l = len(nbh2)
    rand = random.randint(1, 1000)
    if rand < 101:
        board[cur_pos[0]][cur_pos[1]] = 1
    elif 101 < rand < 100 + (50 * nbh_l):
        AIpos = random.choice(nbh)
        board[AIpos[0]][AIpos[1]] = 'AI'
        a = AIpos[0]
        b = AIpos[1]
    elif 100 + (50 * nbh_l) < rand < 150 + (25 * nbh2_l):
        AIpos = random.choice(nbh2)
        board[AIpos[0]][AIpos[1]] = 'AI'
        a = AIpos[0]
        b = AIpos[1]
    print_board(board)
    board[a][b] = 0
    return board


# Transition matrix
def t_matrix():
    valid = []
    p = 0
    t_board = [[0 for x in range(100)] for y in range(100)]
    for i in range(25):
        for j in range(25):
            for z in range(4):
                n = 0
                for d in DIRECTIONS:
                    if on_f_board(i + d[0]*4) and on_f_board(j + d[1]*4):
                        if i + d[0]*4 == n and DIRECTIONS.index(d) == n:
                            t_board[i + d[0] * 4][j + d[1] * 4] = 0.7
                            p = 0.7
                        else:
                            valid.append((i + d[0] * 4, j + d[1] * 4))
                        for v in valid:
                            t_board[v[0]][v[1]] = (1 - p) / len(valid)
                    n += 1
    return t_board

# probability vector
def f_vector():
    f_board = [[float(1/100) for x in range(1)] for y in range(100)]
    return f_board


def o_matrix(cur_pos):
    sensed_board = [[0 for x in range(5)] for y in range(5)]
    a = cur_pos[0]
    b = cur_pos[1]
    sensed_board[a][b] = 0.100
    nbh, nbh2 = sensed_possible_states(cur_pos)
    for i in nbh:
        sensed_board[i[0]][i[1]] = 0.050
    for i in nbh2:
        sensed_board[i[0]][i[1]] = 0.025
    sensed_board[cur_pos[0]][cur_pos[1]] = 0.100
    matrix = [[0 for x in range(100)] for y in range(100)] # creating diognal matrix from our 5x5 matrix
    isb = 0
    isb2 = 0
    end = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                matrix[i][j] = sensed_board[isb2][isb]
                end += 1
                if end == 4:
                    end = 0
                    isb += 1
                    if isb == 5:
                        isb = 0
                        isb2 += 1
    return matrix


def forward_hmm(board):
    current = current_pos(board)
    f = f_vector()
    t = t_matrix()
    o = o_matrix(current)
    y = np.dot(o, t)
    f = np.dot(y, f)
    if sum(f) != 0:
        f /= np.sum(f)  #alpha
    f_print = [[0.0 for x in range(5)] for y in range(5)]
    a, b, n, prob = 0, 0, 0, 0
    for i in f:
        prob += float(i)
        n += 1
        if n == 4:
            f_print[a][b] = float(prob)
            a += 1
            prob = 0
            n = 0
            if a == 5:
                a = 0
                b +=1
    print('------ FORWARD HMM BOARD ------')
    print_board(f_print)


w, h = 5, 5;
board = [[0 for x in range(w)] for y in range(h)]
start = start_pos(board)
cur_dir = start[2]
robot_walk(board, start, cur_dir)
