import unittest
from unittest.mock import patch
from utils import another_utility_function

class TestUtils(unittest.TestCase):
    @patch('random.randint')
    def test_another_utility_function(self, mock_randint):
        mock_randint.side_effect = [1, 2]

        args = 3
        result = another_utility_function(args)
        expected = (1, 2) 

        self.assertEqual(result, expected)

    def test_is_valid_move(self):
        from utils import is_valid_move
        move = (1, 1)
        board_size = 3
        self.assertTrue(is_valid_move(move, board_size))

if __name__ == '__main__':
    unittest.main()
