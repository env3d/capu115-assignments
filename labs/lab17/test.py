import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_Grade(self):
        # Enter code here
        josh = Grade(10, 30, 100)
        amy = Grade(20, 35, 90)
        assert josh.get_exam() > amy.get_exam()
        assert josh.get_final() < amy.get_final()

    def test_UTC_Time(self):
        # Enter code here
        t1 = UTC_Time(12,30)
        assert t1.format_PDT() == '5:30'
        t2 = UTC_Time(1,15)
        assert t2.format_PDT() == '18:15'

    def test_Point(self):
        # Enter code here
        p1 = Point(3,4)
        p2 = Point(0,3)
        p3 = Point(4,0)
        assert p1.getDistanceFromOrigin() == 5
        assert p2.getDistanceFromOrigin() == 3
        assert p3.getDistanceFromOrigin() == 4

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
