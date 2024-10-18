import unittest
from ui.gui_ui import GUIUI

class TestGUIUI(unittest.TestCase):
    def setUp(self):
        self.ui = GUIUI()

    def test_initialize(self):
        self.assertIsNotNone(self.ui.window)

    def test_display_message(self):
        message = "Hello, World!"
        self.ui.display_message(message)
        
if __name__ == '__main__':
    unittest.main()
