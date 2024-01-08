import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_calculate_price(self):
        # Enter code here
        answers = [4.5, 10.8, 17.1]
        assert([ calculate_price(i) for i in range(5,20,7)] == answers)


    def test_better_mark(self):
        # Enter code here
        answers = [50.0, 50.0, 50.0, 75.0, 100.0]
        assert([better_mark(10, i) for i in range(0,41,10) ] == answers)


    def test_volume_of_cylinder(self):
        # Enter code here

        answers = [3.141592653589793, 6.283185307179586, 12.566370614359172, 25.132741228718345]

        user = [volume_of_cylinder(r, h) for r in range(1,3) for h in range(1,3)]
        for i in range(len(answers)):
            assert( abs(answers[i] - user[i]) < 0.000001)

    def test_price_percentage(self):
        # Enter code here

        answers = ['-50.0%', '-45.0%', '-40.0%', '-35.0%', '-30.0%', '-25.0%', '-20.0%', '-15.0%', '-10.0%', '-5.0%', '0.0%', '5.0%', '10.0%', '15.0%', '20.0%', '25.0%', '30.0%', '35.0%', '40.0%', '45.0%']

        assert( [ price_percentage(100, i) for i in range(50, 150, 5) ] == answers )

    def test_compound_interest(self):
        # Enter code here
        answers = [10000.0, 10829.995068075097, 11728.879317453097, 12702.370516206507, 13756.6610043379, 14898.45708301605, 16135.021673099234, 17474.220514294953, 18924.572198827107, 20495.302357872868]
        assert( [compound_interest(i) for i in range(10)] == answers)



    def test_alarm(self):
        # Enter code here
        assert(alarm(0, 3) == 3)
        assert(alarm(23, 3) == 2)

    def test_convert_to_f(self):
        # Enter code here
        assert(convert_to_f(100) == 212)
        assert(convert_to_f(0) == 32)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
