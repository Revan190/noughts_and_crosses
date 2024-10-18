import unittest
from game.player import Player
from game.board import Board

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('X', 'Player 1')
        self.board = Board()

    def test_make_move(self):
        self.player.make_move(self.board, 0)
        self.assertEqual(self.board.board[0], 'X')

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), 'Player 1')

if __name__ == '__main__':
    unittest.main()
