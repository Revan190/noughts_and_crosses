import random
from game.ai_player import AIPlayer

class MediumAI:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def make_move(self, board):
        best_score = float('-inf')
        best_position = None
        for i in range(9):
            if board.board[i] == " ":
                board.make_move(i, self.symbol)
                score = self.minimax(board, 0, False)
                board.undo_move(i)
                if score > best_score:
                    best_score = score
                    best_position = i
        board.make_move(best_position, self.symbol)
        return best_position

    def minimax(self, board, depth, is_maximizing):
        if board.check_winner() == self.symbol:
            return 10 - depth
        elif board.check_winner() != " ":
            return depth - 10
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board.board[i] == " ":
                    board.make_move(i, self.symbol)
                    score = self.minimax(board, depth + 1, False)
                    board.undo_move(i)
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board.board[i] == " ":
                    board.make_move(i, "X")
                    score = self.minimax(board, depth + 1, True)
                    board.undo_move(i)
                    best_score = min(score, best_score)
            return best_score