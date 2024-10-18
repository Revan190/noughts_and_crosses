class ConsoleUI:
    def display(self, board):
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def display_message(self, message):
        print(message)

    def get_player_input(self):
        while True:
            try:
                move = int(input("Enter item number (1-9): ")) - 1
                if move < 0 or move > 8:
                    raise ValueError
                return move
            except ValueError:
                self.display_message("Invalid input. Please try again.")
