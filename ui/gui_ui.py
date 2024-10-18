import tkinter as tk
from tkinter import messagebox

class GUIUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", width=5, height=2, command=lambda x=i, y=j: self.on_button_click(x, y))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, x, y):
        if self.buttons[x][y]['text'] == "":
            self.buttons[x][y]['text'] = self.game.current_player.get_symbol()
            position = x * 3 + y
            if self.game.player.make_move(self.game.board, position):
                winner = self.game.board.check_winner()
                if winner:
                    self.display_winner(winner)
                elif self.game.board.is_full():
                    messagebox.showinfo("Game Over", "The game ended in a draw!")
                else:
                    self.game.switch_player()
                    self.ai_move()

    def ai_move(self):
        position = self.game.ai.make_move(self.game.board)
        x, y = divmod(position, 3)
        self.buttons[x][y]['text'] = self.game.ai.get_symbol()
        winner = self.game.board.check_winner()
        if winner:
            self.display_winner(winner)
        elif self.game.board.is_full():
            messagebox.showinfo("Game Over", "The game ended in a draw!")
        else:
            self.game.switch_player()

    def display_winner(self, winner):
        messagebox.showinfo("Winner", f"Player {winner} won!")
