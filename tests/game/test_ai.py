import unittest
from game.ai_player import AIPlayer
from game.board import Board

class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.ai = AIPlayer('O', 'Computer')
        self.board = Board()

    def test_make_move(self):
        self.board.board = ['X', 'O', 'X', None, None, None, None, None, None]
        position = self.ai.make_move(self.board)
        self.assertIn(position, [3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
