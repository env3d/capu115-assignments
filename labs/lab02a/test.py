import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_depreciate_multiple_years(self):
        # Enter code here
        assert(abs(depreciate_multiple_years(100,5)-59.049) <= 0.0001)

    def test_depreciate_one_year(self):
        # Enter code here
        assert( depreciate_one_year(100) == 90 )

    def test_estimate_dino(self):
        # Enter code here
        assert(abs(estimate_dino(214.44, 1.46, 26) - 24955.535104996252) <= 0.0001)

    def test_estimate_theropoda(self):
        # Enter code here
        assert(abs(estimate_theropoda(1)-0.73) <= 0.0001)

    def test_convert_dollars(self):
        # Enter code here
        assert(abs(convert_dollars(10)-12.9) <= 0.00001)

    def test_convert_mileage(self):
        # Enter code here
        assert(abs(convert_mileage(15)-15.681) <= 0.00001)


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
