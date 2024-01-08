import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_leap_year_div_4_only(self):
        # Enter code here
        for i in range(4,99,4):
            assert(isLeapYear(i))

        for i in range(3,99,4):
            assert(isLeapYear(i) == False)

    def test_leap_year(self):
        # Enter code here
        for i in [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]:
            assert(isLeapYear(i))

    def test_draw_bar_chart_red(self):
        # Enter code here
        from unittest.mock import MagicMock
        t = MagicMock()
        t.color = MagicMock()
        t.fillcolor = MagicMock()
        drawBarChart(t, [200])
        t.color.assert_called_with('red')

    def test_draw_bar_chart_yellow(self):
        # Enter code here
        from unittest.mock import MagicMock
        t = MagicMock()
        t.color = MagicMock()
        t.fillcolor = MagicMock()
        drawBarChart(t, [100])
        t.color.assert_called_with('yellow')

    def test_draw_bar_chart_green(self):
        # Enter code here
        from unittest.mock import MagicMock
        t = MagicMock()
        t.color = MagicMock()
        t.fillcolor = MagicMock()
        drawBarChart(t, [50])
        t.color.assert_called_with('green')



    def test_grade(self):
        # Enter code here
        assert(grade(49) == 'F')
        assert(grade(50) == 'D')
        assert(grade(60) == 'C')
        assert(grade(70) == 'B')
        assert(grade(80) == 'A')


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
