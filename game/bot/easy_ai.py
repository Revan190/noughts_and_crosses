import random
from game.ai_player import AIPlayer

class EasyAI:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def make_move(self, board):
        available_positions = [i for i, x in enumerate(board.board) if x == " "]
        position = random.choice(available_positions)
        board.make_move(position, self.symbol)
        return position