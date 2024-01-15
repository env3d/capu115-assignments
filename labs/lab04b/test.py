import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch


class UnitTests(unittest.TestCase):

    def test_draw_carbon_chain_3(self):
        # Enter code here
        mock_turtle = MagicMock()
        with patch('turtle.Turtle', return_value = mock_turtle):
            draw_carbon_chain(0)
            pendown_alts = ['call.pendown()', 'call.down()', 'call.pd()']
            assert len([i for i in mock_turtle.mock_calls if str(i) in pendown_alts]) == 1, "Bond line not drawn properly and called with draw_carbon_chain(0)"

    def test_draw_carbon_chain_2(self):
        # Enter code here
        num_calls = 5
        with patch('main.draw_letter') as mock_draw_letter:
            with patch('turtle.Turtle'):
                draw_carbon_chain(num_calls)
                assert mock_draw_letter.call_count == num_calls*3+2, "Must draw H at the beginning and end"

    def test_draw_carbon_chain_1(self):
        # Enter code here
        with patch('main.draw_carbons') as mock_draw_carbons:
            with patch('turtle.Turtle'):
                draw_carbon_chain(5)
                mock_draw_carbons.assert_called_once()

    def test_draw_carbons_2(self):
        # Enter code here
        with patch('main.draw_carbon') as mock_draw_carbon:
            mock_turtle = MagicMock()
            draw_carbons(mock_turtle, 10)
            pendown_alts = ['call.pendown()', 'call.down()', 'call.pd()']
            assert 9 <= len([i for i in mock_turtle.mock_calls if str(i) in pendown_alts]) <= 10 , "Number of lines draw not correct"

    def test_draw_carbons_1(self):
        # Enter code here
        with patch('main.draw_carbon') as mock_draw_carbon:
            mock_turtle = MagicMock()
            draw_carbons(mock_turtle, 10)
            assert mock_draw_carbon.call_count == 10

    def test_draw_carbon_2(self):
        # Enter code here
        with patch('main.draw_letter') as mock_draw_letter:
            mock_turtle = MagicMock()
            draw_carbon(mock_turtle)
            pendown_alts = ['call.pendown()', 'call.down()', 'call.pd()']
            assert len([i for i in mock_turtle.mock_calls if str(i) in pendown_alts]) == 2, "Must draw 2 lines"

    def test_draw_carbon_1(self):
        # Enter code here
        with patch('main.draw_letter') as mock_draw_letter:
            mock_turtle = MagicMock()
            draw_carbon(mock_turtle)
            assert mock_draw_letter.call_count == 3, mock_draw_letter.mock_calls

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
