import unittest
from main import *

# Add imports here
import unittest
from main import *
# Add imports here
from unittest.mock import patch
from unittest.mock import Mock

class MyTurtle(Mock):

    def reset(self):
        self.total_forward = 0
        self.total_angle = 0
        self.total_dots = 0
        self.total_circles = 0

    def forward(self, v): self.total_forward += 1
    def backward(self, v): self.total_forward -= 1
    def left(self, v): self.total_angle += v
    def right(self, v): self.total_angle -= v
    def dot(self, v=1): self.total_dots += 1
    def circle(self, v, a): self.total_circles += 1
    def xcor(self): return 0
    def ycor(self): return 0

def draw_letter(t, letter):

    if letter in draw_letter.calls:
        draw_letter.calls[letter] += 1
    else:
        draw_letter.calls[letter] = 1

draw_letter.calls = {}


class UnitTests(unittest.TestCase):

    def setUp(self):
        # Add setup code here
        self.myturtle = MyTurtle()
        self.myturtle.reset()

    def test_rainbow2(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            rainbow2()
            assert(self.myturtle.total_circles == 7)

    def test_rainbow1(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            rainbow1()
            assert(self.myturtle.total_circles == 2)

    def test_exercise3(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            with patch('main.draw_letter') as draw_letter:
                draw_letter.side_effect=draw_letter
                for i in range(10):
                    self.myturtle.reset()
                    draw_letter.calls = {}
                    exercise3(i)
                    assert(len(draw_letter.calls.keys()) == i)
                    assert(self.myturtle.total_forward == i)

    def test_exercise2(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            exercise2()

        assert(self.myturtle.total_forward == 4)

    def test_exercise1(self):
        # Enter code here
        with patch.object(turtle, 'Turtle', return_value=self.myturtle):
            exercise1()

        assert(self.myturtle.total_forward >= 3)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
