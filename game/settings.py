class Settings:
    def __init__(self):
        self.player_symbol = 'X'
        self.ai_symbol = 'O'
        self.total_games = 1

    def set_player_symbol(self, symbol):
        self.player_symbol = symbol

    def set_ai_symbol(self, symbol):
        self.ai_symbol = symbol

    def set_total_games(self, total):
        self.total_games = total
