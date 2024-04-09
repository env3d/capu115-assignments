import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch

class UnitTests(unittest.TestCase):

    def test_print_names(self):
        # Enter code here
        with patch('builtins.print') as mock_print:
            print_names()
        assert 'Jack' in [c[1][0] for c in mock_print.mock_calls]
        assert 'Ouack' in [c[1][0] for c in mock_print.mock_calls]
        assert 'Quack' in [c[1][0] for c in mock_print.mock_calls]



    def test_print_12x12(self):
        # Enter code here
        with patch('builtins.print') as mock_print:
            print_12x12()

        #assert False, mock_print.mock_calls
        params = [(c[1][0],c[2]['end']) for c in mock_print.mock_calls if len(str(c[1][0])) > 0]
        num_spaces = len(str(params[0][0])) + len(params[0][1])
        for p in params:
            assert len(str(p[0]))+len(p[1]) == num_spaces

    def test_reverse(self):
        # Enter code here
        assert reverse('hello') == 'olleh'
        assert reverse('abcde fg') == 'gf edcba'

    def test_palindromes(self):
        # Enter code here
        assert palindromes('pap')
        assert not palindromes('papa')

    def test_remove_dups(self):
        # Enter code here
        assert remove_dup('abcde abcde') == 'abcde '
        assert remove_dup('abcde ddddd') == 'abcde '
        assert remove_dup('abcde ddddd eeeee') == 'abcde '

    def test_lengthOfLastWord(self):
        # Enter code here
        assert lengthOfLastWord("Hello World") == 5
        assert lengthOfLastWord("   fly me   to   the moon  ") == 4
        assert lengthOfLastWord("luffy is still joyboy") == 6

    def test_canConstruct(self):
        # Enter code here
        assert not canConstruct('a', 'b')
        assert not canConstruct('aa', 'ab')
        assert canConstruct('aa', 'aab')

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
