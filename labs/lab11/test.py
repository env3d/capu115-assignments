import unittest
from main import *

# Add imports here
from unittest.mock import patch, MagicMock

class UnitTests(unittest.TestCase):

    def test_dna_to_code(self):
        # Enter code here
        assert(dna_to_code('A') == '10')
        assert(dna_to_code('T') == '00')
        assert(dna_to_code('G') == '11')
        assert(dna_to_code('C') == '01')


    def test_draw_coded(self):
        # Enter code here
        with patch('main.draw_0') as mock_draw_0:
            with patch('main.draw_1') as mock_draw_1:
                draw_coded('0001','red')
                assert(len(mock_draw_0.mock_calls) == 3)
                assert(len(mock_draw_1.mock_calls) == 1)


    def test_visualize(self):
        # Enter code here
        with patch('main.draw_coded') as mock_draw_coded:
            with patch('main.dna_to_code') as mock_dna_to_code:
                visualize('ATGC', 'blue')
                #assert(mock_dna_to_code.called_once())
                #assert(mock_draw_coded.called_once())
                assert len(mock_dna_to_code.mock_calls) == 1
                assert len(mock_draw_coded.mock_calls) == 1


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
