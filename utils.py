import random

def another_utility_function(args):
    board_size = args
    return (random.randint(0, board_size - 1), random.randint(0, board_size - 1))

def is_valid_move(move, board_size):
    return isinstance(move, tuple) and len(move) == 2 and \
           0 <= move[0] < board_size and 0 <= move[1] < board_size

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(len(board)):
        if all(row[col] == symbol for row in board):
            return True
    if all(board[i][i] == symbol for i in range(len(board))) or \
       all(board[i][len(board) - 1 - i] == symbol for i in range(len(board))):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_coordinates(input_str):
    try:
        x, y = map(int, input_str.split(","))
        return (x, y)
    except ValueError:
        return None

def display_message(message):
    print(message)
