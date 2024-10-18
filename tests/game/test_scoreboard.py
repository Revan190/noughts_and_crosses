import unittest
from game.scoreboard import Scoreboard

class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_add_score(self):
        self.scoreboard.add_score('Player 1', 1)
        self.assertEqual(self.scoreboard.get_score('Player 1'), 1)

    def test_get_scores(self):
        self.scoreboard.add_score('Player 1', 1)
        self.scoreboard.add_score('Player 2', 2)
        scores = self.scoreboard.get_scores()
        self.assertEqual(scores, {'Player 1': 1, 'Player 2': 2})

    def test_reset_scores(self):
        self.scoreboard.add_score('Player 1', 1)
        self.scoreboard.reset_scores()
        self.assertEqual(self.scoreboard.get_scores(), {})

if __name__ == '__main__':
    unittest.main()
