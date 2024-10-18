class Player:
    def __init__(self, symbol, name="Player"):
        self.symbol = symbol
        self.name = name

    def make_move(self, board, position):
        return board.make_move(position, self.symbol)

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol
