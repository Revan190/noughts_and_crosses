import unittest
from io import StringIO
import sys
from ui.console_ui import ConsoleUI
class TestConsoleUI(unittest.TestCase):
    def setUp(self):
        self.ui = ConsoleUI()
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display_board(self):
        board = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
        self.ui.display_board(board)
        output = self.output.getvalue().strip()
        expected_output = "X O  \n  X O\nO  X"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
