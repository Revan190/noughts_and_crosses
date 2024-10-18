import unittest
from game.game import Game
from game.board import Board

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_switch_player(self):
        initial_player = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(initial_player, self.game.current_player)

    def test_check_winner(self):
        self.game.board.board = ['X', 'X', 'X', None, None, None, None, None, None]
        self.assertEqual(self.game.board.check_winner(), 'X')

    def test_undo_move(self):
        self.game.player.make_move(self.game.board, 0)
        self.game.undo_move()
        self.assertIsNone(self.game.board.board[0])

if __name__ == '__main__':
    unittest.main()
