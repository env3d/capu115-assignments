import unittest
from main import *

from unittest.mock import Mock

class MyTurtle(Mock):

    def reset(self):
        self.total_forward = 0
        self.total_angle = 0
        self.total_dots = 0

    def forward(self, v): self.total_forward += v
    def backward(self, v): self.total_forward -= v
    def left(self, v): self.total_angle += v
    def right(self, v): self.total_angle -= v
    def dot(self, v=1): self.total_dots += 1

from unittest.mock import patch

class UnitTests(unittest.TestCase):

    def setUp(self):
        # Add setup code here
        self.myturtle = MyTurtle()
        self.myturtle.reset()

    def test_polygon(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawPolygon(60, 10)

        assert(self.myturtle.total_forward == 600)
        assert(abs(abs(self.myturtle.total_angle)-360) <= 0.00001)

    def test_rectangle_total_angle(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawRectangle(0, 0)

        assert(abs(abs(self.myturtle.total_angle)-360) <= 0.00001)

    def test_square_total_angle(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawSquare(0)

        assert(abs(abs(self.myturtle.total_angle)-360) <= 0.00001)

    def test_square_total_forward(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawSquare(10)

        assert(self.myturtle.total_forward == 40)


    def test_triangle_total_angle(self):
        # Enter code here
        length = 0
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawTriangle(length)

        assert(abs(abs(self.myturtle.total_angle)-360) < 0.0001)

    def test_triangle_total_forward(self):
        # Enter code here
        length = 30
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawTriangle(length)

        assert(abs(self.myturtle.total_forward) == length * 3)

    def test_rectangle_total_forward(self):
        # Enter code here

        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            drawRectangle(10, 30)

        assert(self.myturtle.total_forward == 80)



    def test_concentric_triangle(self):
        # Enter code here
        num_calls = 0

        def add(side): nonlocal num_calls; num_calls = num_calls+1

        with unittest.mock.patch('main.drawTriangle') as drawTriangle:
            with patch.object(turtle, 'Turtle', return_value=self.myturtle):
                drawTriangle.side_effect = add

                for i in range(50):
                    self.myturtle.reset()
                    num_calls = 0

                    with patch.object(turtle, 'Turtle', return_value=self.myturtle):
                        drawConcentricTriangle(i)

                    assert(num_calls == i or self.myturtle.total_angle == i*360)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
