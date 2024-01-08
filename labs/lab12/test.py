import unittest
from main import *

# Add imports here
from unittest.mock import patch, Mock, MagicMock


class UnitTests(unittest.TestCase):

    def test_palindrome(self):
        # Enter code here
        with patch('main.palindrome', side_effect=palindrome) as mock_func:
            assert mock_func("abba") == True
            assert len(mock_func.mock_calls) >= 2

        with patch('main.palindrome', side_effect=palindrome) as mock_func:
            assert mock_func("abca") == False
            assert len(mock_func.mock_calls) == 2

    def test_countw(self):
        # Enter code here
        with patch('main.countw', side_effect=countw) as mock_func:
            assert mock_func("awwawwaww") == 6
            assert len(mock_func.mock_calls) >= 9

    def test_reverse(self):
        # Enter code here
        with patch('main.reverse', side_effect=reverse) as mock_func:
            l = mock_func([1,2,3,4,5])
            assert l == [5,4,3,2,1]
            assert len(mock_func.mock_calls) >= 5

    def test_square_lst(self):
        # Enter code here
        with patch('main.square_lst', side_effect=square_lst) as mock_func:
            a = mock_func([1,2,3,4,5])
            assert a == [1,4,9,16,25]
            assert len(mock_func.mock_calls) >= 5

    def test_factorial(self):
        # Enter code here
        #assert factorial(5) == 120
        #assert factorial(10) == 3628800
        with patch('main.factorial', side_effect=factorial) as fact:
            a = fact(10)
            assert a == 3628800
            assert len(fact.mock_calls) >= 10

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
