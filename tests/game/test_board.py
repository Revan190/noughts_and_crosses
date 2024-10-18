import unittest
from game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_display_board(self):
        self.board.board = ['X', 'O', 'X', None, None, None, None, None, None]
        self.assertEqual(self.board.display(), 'X O X\n . . .\n . . .')

    def test_is_full(self):
        self.board.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        self.assertTrue(self.board.is_full())

    def test_check_winner(self):
        self.board.board = ['X', 'X', 'X', None, None, None, None, None, None]
        self.assertEqual(self.board.check_winner(), 'X')

    def test_make_move_invalid(self):
        with self.assertRaises(ValueError):
            self.board.make_move(9, 'X')


if __name__ == '__main__':
    unittest.main()
