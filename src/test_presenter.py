from pathlib import Path
import unittest

from presenter import Presenter

class TestPresenter(unittest.TestCase):
    def setUp(sefl):
        font_path = Path("fonts/libtcod/dejavu10x10_gs_tc.png")
        self.presenter = Presenter(window_width=80, window_height=50, window_title="JMC Test", font_path = font_path)

    def test_init(self):
        self.assertTrue(self.presenter.is_window_open())

if __name__ == '__main__':
    unittest.main()
