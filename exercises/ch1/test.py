import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_pair_die(self):
        # Enter code here
        random.seed(0)
        answers = [27, 11, 33, 23, 28, 26]
        results = [ pair_die() for i in range(6) ]
        assert(results == answers)

    def test_die(self):
        # Enter code here
        random.seed(0)
        answers = [1, 2, 1, 3, 5, 4]
        results = [ die(i+1) for i in range(6) ]
        assert(answers == results)

    def test_random_integer(self):
        # Enter code here
        random.seed(0)
        answers = [4, 4, 1, 3 ,5, 4]
        results = [ random_integer() for i in range(6) ]
        assert(answers == results)

    def test_intersect_circle(self):
        # Enter code here
        assert(intersect_circle(0,0,1,3,4,1) == False)
        assert(intersect_circle(0,0,3,3,4,3) == True)

    def test_distance_between_points(self):
        # Enter code here
        assert(distance_between_points(0,0,3,4) == 5)
        assert(distance_between_points(3,4,3,4) == 0)

    def test_distance_from_origin(self):
        # Enter code here
        assert(distance_from_origin(3,4) == 5)
        assert(distance_from_origin(0,0) == 0)

    def test_runway(self):
        # Enter code here
        assert(runway(270) == 27)
        assert(runway(79) == 8)

    def test_remaining_cookies(self):
        # Enter code here
        assert(remaining_cookies(10,5) == 0)
        assert(remaining_cookies(10,9) == 1)

    def test_divide_cookies(self):
        # Enter code here
        assert(divide_cookies(10,5) == 2)
        assert(divide_cookies(10,9) == 1)


    def test_three_average(self):
        # Enter code here
        assert(three_average(0,0,0) == 0)
        assert(three_average(10,20,30) == 20)


    def test_area_rect(self):
        # Enter code here
        assert(area_rect(0,10) == 0)
        assert(area_rect(5,6) == 30)
        assert(area_rect(10,10) == 100)


    def test_convert_to_c(self):
        # Enter code here
        assert(convert_to_c(32) == 0)
        assert(convert_to_c(212) == 100)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
