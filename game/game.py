from game.board import Board
from game.player import Player
from game.ai_player import AIPlayer
from game.bot.easy_ai import EasyAI
from game.bot.medium_ai import MediumAI
from game.bot.hard_ai import HardAI

class Game:
    def __init__(self, ai_level='easy'):
        self.board = Board()
        self.player = Player('X', "Player")
        if ai_level == 'easy':
            self.ai = EasyAI('O', "Computer")
        elif ai_level == 'medium':
            self.ai = MediumAI('O', "Computer")
        else:
            self.ai = HardAI('O', "Computer")
        self.current_player = self.player
        self.move_history = []

    def switch_player(self):
        self.current_player = self.ai if self.current_player == self.player else self.player

    def undo_move(self):
        if self.move_history:
            last_move = self.move_history.pop()
            self.board.undo_move(last_move)
            self.switch_player()
            print(f"The move is cancelled. Now it's {self.current_player.get_name()}'s turn.")
        else:
            print("There are no undo moves available.")

    def play(self):
        while not self.board.is_full():
            self.board.display()
            if self.current_player == self.player:
                self.player_turn()
            else:
                self.ai_turn()

    def player_turn(self):
        try:
            position = input(f"{self.player.get_name()}, select position (0-8) or 'u' to cancel: ")
            if position.lower() == 'u':
                self.undo_move()
                return
            position = int(position)
            if position < 0 or position > 8:
                raise ValueError("The position must be in the range from 0 to 8.")
            if self.player.make_move(self.board, position):
                self.move_history.append(position)
                self.check_game_status()
            else:
                print("This position has already been taken. Try again.")
        except ValueError as e:
            print(f"Error: {e}. Try again.")

    def ai_turn(self):
        print(f"{self.ai.get_name()} makes a move...")
        position = self.ai.make_move(self.board)
        self.move_history.append(position)
        self.check_game_status()

    def check_game_status(self):
        winner = self.board.check_winner()
        if winner:
            self.board.display()
            print(f"Player {winner} won!")
            return
        if self.board.is_full():
            self.board.display()
            print("The game ended in a draw!")
            return
        self.switch_player()
