from game.board import Board
from game.player import Player
from ui.console_ui import ConsoleUI

def main():
    console_ui = ConsoleUI()
    board = Board()
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    current_player = player1

    while True:
        console_ui.display(board.get_state())
        move = console_ui.get_player_input()
        if board.make_move(move, current_player.symbol):
            if board.check_winner(current_player.symbol):
                console_ui.display(board.get_state())
                console_ui.display_message(f"{current_player.name} won!")
                break
            elif board.is_full():
                console_ui.display_message("Draw!")
                break
            current_player = player2 if current_player == player1 else player1
        else:
            console_ui.display_message("Incorrect move, try again.")

if __name__ == "__main__":
    main()
