import unittest
from main import *

# Add imports here
from unittest.mock import patch, MagicMock, mock_open


class UnitTests(unittest.TestCase):

    def test_count_titles(self):
        # Enter code here

        fake_titles = '\n'.join(
          ["1 2 3 4 0 6 7 8 9"]*10 + ["1 2 3 4 1 6 7 8 9"]*5
        )
        with patch("builtins.open", mock_open(read_data=fake_titles)):
            n = count_titles()
        assert(n == 15), n

    def test_count_adult_titles(self):
        # Enter code here
        fake_titles = '\n'.join(
          ["1 2 3 4 0 6 7 8 9"]*10 + ["1 2 3 4 1 6 7 8 9"]*5
        )
        with patch("builtins.open", mock_open(read_data=fake_titles)):
            n = count_adult_titles()
        assert(n == 5), n

    def test_count_romance_titles(self):
        # Enter code here
        fake_titles = '\n'.join(
          ["1 2 3 4 0 6 7 8 Romance,abc"]*5 + ["1 2 3 4 1 6 7 8 abc,Romance"]*5 + ["1 2 3 4 1 6 7 8 abc"]*5
        )
        with patch("builtins.open", mock_open(read_data=fake_titles)):
            n = count_romance_titles()
        assert(n == 10), n

    def test_find_title_id(self):
        # Enter code here
        fake_titles = '\n'.join(
          ["1 2 3 4 0 6 7 8 Romance,abc"]*5 + ["1 2 3 4 1 6 7 8 abc,Romance"]*5 + ["t1 t2 t3 t4 t5 t6 t7 t8 t9"] + ["1 2 3 4 1 6 7 8 abc"]*5
        )
        with patch("builtins.open", mock_open(read_data=fake_titles)):
            n = find_title_id('t3')
            d = find_title_id('aaa')
        assert(n == 't1'), n
        assert(d == ''), d

    def test_get_rating(self):
        # Enter code here
        fake_titles = '\n'.join(
          ["1 2 3 4 0 6 7 8 Romance,abc"]*5 + ["1 2 3 4 1 6 7 8 abc,Romance"]*5 + ["t1 10 t3 t4 t5 t6 t7 t8 t9"] + ["1 2 3 4 1 6 7 8 abc"]*5
        )
        with patch("builtins.open", mock_open(read_data=fake_titles)):
            with patch("main.find_title_id", return_value='t1'):
                n = get_rating('t3')
                assert(n == '10' or n == 10), 'Not returning the correct rating'
            with patch("main.find_title_id", return_value='aaa'):
                d = get_rating('aaa')
                assert(d == -1), 'When title not found, need to return -1'

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
