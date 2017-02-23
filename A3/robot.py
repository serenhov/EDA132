import random
import numpy as np

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
    while i < 30:
        board, current_pos = the_move(board, current_pos, cur_dir)
        print_board(board)
        i += 1

def sensed_possible_moves(board, player):
    valid_moves = []
    for j in range(5):
        for i in range(5):
            if board[i][j] == player:
                for d in DIRECTIONS:
                    new_row = i + d[0]
                    new_column = j + d[1]
                    while on_board(new_row) and on_board(new_column):
                        if board[new_row][new_column] == -player:
                            new_row += d[0]
                            new_column += d[1]
                            if on_board(new_row) and on_board(new_column) and board[new_row][new_column] == 0:
                                if (new_row, new_column) not in valid_moves:
                                    valid_moves.append((new_row, new_column))
                                break
                        else:
                            break
    return valid_moves

def sensor(cur_pos):
    sensed_board = [[0 for x in range(5)] for y in range(5)]
    sensed_board[cur_pos[0]][cur_pos[1]] = 0.100




w, h = 5, 5;
board = [[0 for x in range(w)] for y in range(h)]
start = start_pos(board)
cur_dir = start[2]
robot_walk(board, start, cur_dir)