import random
from player import Player

class AIPlayer(Player):
    def make_move(self, board):
        available_positions = board.get_available_moves()
        if available_positions:
            position = random.choice(available_positions)
            board.make_move(position, self.symbol)
