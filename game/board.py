class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 

    def display(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, position, symbol):
        if self.board[position] == ' ':
            self.board[position] = symbol
            return True
        return False

    def undo_move(self, position):
        self.board[position] = ' '

    def check_winner(self, symbol):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if all(self.board[i] == symbol for i in combo):
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def copy(self):
        new_board = Board()
        new_board.board = self.board.copy()
        return new_board

    def get_opponent(self, symbol):
        return 'O' if symbol == 'X' else 'X'

    def get_state(self):
        return self.board
