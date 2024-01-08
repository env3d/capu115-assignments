import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch

class UnitTests(unittest.TestCase):

    def test_drawFiveStars(self):
        # Enter code here
        mock_turtle = MagicMock()
        with patch('turtle.Turtle', return_value = mock_turtle) as mock_turtle_class:
            with patch('main.drawFivePointStar') as mock_star:
                drawFiveStars()
                mock_turtle_class.assert_called_once()
                assert mock_star.call_count == 5, "Must call drawSquareFromCenter the correct number of times"
                assert len([i for i in mock_turtle.method_calls if str(i).startswith('call.penup')]) == 5
                assert len([i for i in mock_turtle.method_calls if str(i).startswith('call.pendown')]) == 5
                assert len([i for i in mock_turtle.method_calls if str(i).startswith('call.forward')]) == 5
                assert len([i for i in mock_turtle.method_calls if str(i).startswith('call.right')]) == 5

    def test_drawPattern(self):
        # Enter code here
        mock_turtle = MagicMock()
        with patch('turtle.Turtle', return_value = mock_turtle) as mock_turtle_class:
            with patch('main.drawSquareFromCenter') as mock_square:
                drawPattern(5)
                mock_turtle_class.assert_called_once()
                assert mock_square.call_count == 5, "Must call drawSquareFromCenter the correct number of times"
                assert len([i for i in mock_turtle.method_calls if str(i).startswith('call.left')]) == 5 or len([i for i in mock_turtle.method_calls if str(i).startswith('call.right')]) == 5


    def test_drawConcentricSquare(self):
        # Enter code here
        mock_turtle = MagicMock()
        with patch('turtle.Turtle', return_value = mock_turtle) as mock_turtle_class:
            with patch('main.drawSquare') as mock_square:
                drawConcentricSquare()
                mock_turtle_class.assert_called_once()
                assert mock_square.call_count == 5, "Must call drawSquare the correct number of times"
                assert len([i for i in mock_turtle.method_calls if str(i) == 'call.penup()']) == 5
                assert len([i for i in mock_turtle.method_calls if str(i) == 'call.pendown()']) == 5
                assert [20,40,60,80,100] == [i[1][1] for i in mock_square.mock_calls], "Not calling drawSquare with the right parameters"

    def test_drawConcentricTriangles2(self):
        # Enter code here
        mock_turtle = MagicMock()
        with patch('turtle.Turtle', return_value = mock_turtle) as mock_turtle_class:
            with patch('main.drawTriangle2') as mock_triangles:
                drawConcentricTriangles2(10)
                mock_turtle_class.assert_called_once()
                assert mock_triangles.call_count == 10, "Must call drawTriangles2 the correct number of times"
                assert len([i for i in mock_turtle.method_calls if str(i) == 'call.penup()']) == 10
                assert len([i for i in mock_turtle.method_calls if str(i) == 'call.pendown()']) == 10

    def test_drawConcentricTriangles(self):
        # Enter code here
        with patch('main.drawTriangle') as mock_triangle:
            drawConcentricTriangles(5)
            assert mock_triangle.call_count == 5, "Must call drawTriangle in a loop for the correct number of times"

        with patch('main.drawTriangle') as mock_triangle:
            drawConcentricTriangles(10)
            assert mock_triangle.call_count == 10, "Must call drawTriangle in a loop for the correct number of times"

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
