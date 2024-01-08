import unittest
from main import *

# Add imports here
from unittest.mock import mock_open, patch

class UnitTests(unittest.TestCase):

    def test_get_frequent_words(self):
        # Enter code here
        data = "spam a b c d e\nham d e\nspam a b\nham d e\nspam a"

        with patch('builtins.open', mock_open(read_data=data)):
            d = get_frequent_words(3)
            assert 'a' in d
            assert 'b' not in d
            assert 'c' not in d


    def test_get_unique_spam(self):
        # Enter code here
        def test_get_ham_dictionary(self):
        # Enter code here
            data = "spam a b c d e\nham d e\nspam a b\nham d e\nspam a"

            with patch('builtins.open', mock_open(read_data=data)):
                d = get_unique_spam()
                assert 'd' not in d
                assert 'e' not in d
                assert d['a'] == 3
                assert d['b'] == 2
                assert d['c'] == 1


    def test_get_ham_dictionary(self):
            # Enter code here
        data = "spam a b c d e\nham d e\nspam a b\nham d e\nspam a"

        with patch('builtins.open', mock_open(read_data=data)):
            d = get_ham_dictionary()
            assert d['d'] == 2
            assert d['e'] == 2


    def test_get_spam_dictionary(self):
        # Enter code here
        data = "spam a b c d e\nham d e\nspam a b\nham d e\nspam a"

        with patch('builtins.open', mock_open(read_data=data)):
            d = get_spam_dictionary()
            assert d['a'] == 3
            assert d['b'] == 2
            assert d['c'] == 1


    def test_count_spam(self):
        # Enter code here
        data = "spam 1\nham 2\nspam 3\nham 4\nspam 5"

        with patch('builtins.open', mock_open(read_data=data)):
            assert(count_spam() == 3)


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
