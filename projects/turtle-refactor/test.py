import unittest
from main import *

# Add imports here
from unittest.mock import patch, MagicMock

class UnitTests(unittest.TestCase):

    def test_only_one_turtle(self):
        # Enter code here
        with patch('turtle.Turtle') as mock_turtle:
            draw_picture()
            assert len([x for x in mock_turtle.mock_calls if x[0] == '']) == 1, "You must create exactly 1 turtle, no more, no less"

    def test_draw_circles4_not_called(self):
        # Enter code here
        with patch('main.drawCircles4') as mock_drawCircles4:
            with patch('turtle.Turtle') as mock_turtle:
                draw_picture()
                assert len(mock_drawCircles4.mock_calls) == 0, "You must create a new drawCircle"

    def test_draw_special_not_called(self):
        # Enter code here
        with patch('main.drawSpecial4') as mock_drawSpecial:
            with patch('turtle.Turtle') as mock_turtle:
                draw_picture()
                assert len(mock_drawSpecial.mock_calls) == 0, "You must create a new drawSpecial"

    def test_drawCircles_defined(self):
        # Enter code here
        drawCirclesFunctions = [x for x in list(globals()) if 'drawCircles' in x ]
        # delete all the predefined drawCircles
        for x in [4,5,10,19,20]:
            drawCirclesFunctions.remove('drawCircles'+str(x))

        assert len(drawCirclesFunctions) == 1, "You must define a single new drawCircles function"

    def test_drawSpecial_defined(self):
        # Enter code here
        drawSpecialFunctions = [x for x in list(globals()) if 'drawSpecial' in x ]
        # delete all the predefined drawCircles
        for x in [4,5,10,19,20]:
            drawSpecialFunctions.remove('drawSpecial'+str(x))

        #assert len(drawSpecialFunctions) == 1, "You must define a single new drawSpecial function"
        assert len(drawSpecialFunctions) == 1, ("You must define a single new drawSpecial function", drawSpecialFunctions)

    def test_total_num_of_circles_drawn(self):
        # Enter code here
        with patch('turtle.Turtle') as mock_turtle:
            draw_picture()
            assert len([x[0] for x in mock_turtle.mock_calls if 'circle' in x[0]]) == 260, "Total number of circles must match the original version"

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
