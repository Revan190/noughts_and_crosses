import unittest
from game.bot.medium_ai import MediumAI

class TestMediumAI(unittest.TestCase):
    def setUp(self):
        self.ai = MediumAI()

    def test_make_move(self):
        board = [[' ' for _ in range(3)] for _ in range(3)]
        move = self.ai.make_move(board)
        self.assertIn(move, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])

if __name__ == '__main__':
    unittest.main()
