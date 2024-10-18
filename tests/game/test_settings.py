import unittest
from game.settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_default_settings(self):
        self.assertEqual(self.settings.board_size, 3)
        self.assertEqual(self.settings.player_symbols, ['X', 'O'])
        self.assertEqual(self.settings.max_score, 5)

    def test_change_settings(self):
        self.settings.board_size = 4
        self.settings.player_symbols = ['A', 'B']
        self.settings.max_score = 10

        self.assertEqual(self.settings.board_size, 4)
        self.assertEqual(self.settings.player_symbols, ['A', 'B'])
        self.assertEqual(self.settings.max_score, 10)

    def test_invalid_settings(self):
        with self.assertRaises(ValueError):
            self.settings.board_size = -1

if __name__ == '__main__':
    unittest.main()
