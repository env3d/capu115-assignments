import unittest
from main import *

# Add imports here
epsilon = 0.0000001

class UnitTests(unittest.TestCase):

    def test_pounds_to_kilos_range(self):
        # Enter code here
        for i in range(1,10):
            assert(abs(pounds_to_kilos(i*2.2)-i) <= epsilon )

    def test_inch_to_cm_0(self):
        # Enter code here
        assert(inches_to_centimeters(0) == 0)

    def test_inch_to_cm_range(self):
        # Enter code here
        for i in range(1, 10):
            assert(abs(inches_to_centimeters(i) - i*2.54) <= epsilon)

    def test_bmr_m(self):
        # Enter code here
        def male_bmr(weight, height, age): return 66 + 13.7 * weight + 5 * height - 6.8 * age

        for i in range(100):
            assert(abs(calculate_bmr(i,i,'M',i) - male_bmr(i,i,i)) <= epsilon )

    def test_bmr_f(self):
        # Enter code here
        def female_bmr(weight, height, age): return 655 +  9.6 * weight + 1.8 * height - 4.7 * age

        for i in range(100):
            assert(abs(calculate_bmr(i,i,'F',i) - female_bmr(i,i,i)) <= epsilon )

    def test_activity_expenditure(self):
        # Enter code here
        for i in range(100):
            assert( abs(calculate_activity_expenditure(i, 0.55) - i*0.55) <= epsilon )

    def test_food_expenditure(self):
        # Enter code here
        for i in range(100):
            assert(abs(calculate_food_expenditure(i) - i*0.05) <= epsilon)

    def test_pounds_to_kilos_0(self):
        # Enter code here
        assert(abs(pounds_to_kilos(0) == 0))
    
if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
