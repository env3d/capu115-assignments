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
        self.total_penup = 0
        self.total_pendown = 0

    def forward(self, v): self.total_forward += v
    def backward(self, v): self.total_forward -= v
    def left(self, v): self.total_angle += v
    def right(self, v): self.total_angle -= v
    def dot(self, v=1): self.total_dots += 1
    def penup(self): self.total_penup += 1
    def pendown(self): self.total_pendown += 1


class UnitTests(unittest.TestCase):

    def setUp(self):
        # Add setup code here


        self.myturtle = MyTurtle()
        self.myturtle.reset()

    def test_draw_row_0(self):
        # Enter code here
        draw_row(self.myturtle, 0)
        assert(abs(self.myturtle.total_dots) == 0)

    def test_draw_row_multiple(self):
        # Enter code here

        for i in range(1,10):
            self.myturtle.reset()
            draw_row(self.myturtle, i)
            assert(abs(self.myturtle.total_dots) == i)

    def test_draw_triangle_num_dots(self):
        # Enter code here

        acc = 0
        for i in range(1,4):
            acc += i
            self.myturtle.reset()
            draw_triangle(self.myturtle, i)
            assert(abs(self.myturtle.total_dots) == acc)



    def test_test_upside_down_num_dots(self):
        # Enter code here

        acc = 0
        for i in range(1,4):
            acc += i
            self.myturtle.reset()
            draw_upsidedown_triangle(self.myturtle, i)
            assert(abs(self.myturtle.total_dots) == acc)



    def test_draw_diamond_odd(self):
        # Enter code here
        self.myturtle.reset()
        draw_diamond(self.myturtle, 3)
        assert(abs(self.myturtle.total_dots) == 4)

        self.myturtle.reset()
        draw_diamond(self.myturtle, 5)
        assert(abs(self.myturtle.total_dots) == 9)



    def test_draw_diamond_even(self):
        # Enter code here
        self.myturtle.reset()
        draw_diamond(self.myturtle, 4)
        assert(abs(self.myturtle.total_dots) == 6)

        self.myturtle.reset()
        draw_diamond(self.myturtle, 6)
        assert(abs(self.myturtle.total_dots) == 12)

    def test_draw_triangle_called_draw_row(self):
        # Enter code here
        with patch('main.draw_row') as draw_row:
            draw_triangle(self.myturtle, 5)
            assert(draw_row.called)


    def test_draw_upsidedown_triagle_called_draw_row(self):
        # Enter code here
        with patch('main.draw_row') as draw_row:
            draw_upsidedown_triangle(self.myturtle, 5)
            assert(draw_row.called)


    def test_draw_diamond_called_other_functions(self):
        # Enter code here
        with patch('main.draw_triangle') as draw_triangle:
            with patch('main.draw_upsidedown_triangle') as draw_upsidedown_triangle:
                draw_diamond(self.myturtle, 5)
                assert(draw_triangle.called)
                assert(draw_upsidedown_triangle.called)


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
