import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_calculate_price_have_remaining(self):
        # Enter code here

        assert(abs(calculate_price(7)-( (6*1.25) + 1.50)) < 0.0000001)


    def test_distance_SCIENCE_WORLD_LANGARA(self):
        # Enter code here
        assert(abs(distance(49.272967, -123.101732, 49.225798, -123.108383)-5200) < 70)

    def test_caluclate_price_non_3_multiple(self):
        # Enter code here
        assert(abs(calculate_price(2)-(2*1.5)) < 0.0000001)

    def test_caluclate_price_3_multiple(self):
        # Enter code here
        assert(abs(calculate_price(6)-(6*1.25)) < 0.0000001)

    def test_cone_surface_area(self):
        # Enter code here
        def answer(r, h):
            return (math.pi*r) * (r + math.sqrt(math.pow(h,2)+math.pow(r,2)))

        assert(abs(answer(5,10)-cone_surface_area(5,10)) <= 0.00001)

    def test_midterms_weighted(self):
        # Enter code here
        assert( abs(midterms_weighted(5,10,20,40)-10) <= 0.00001)

    def test_calculate_average(self):
        # Enter code here
        assert(abs(calculate_average(5,10,20,40)-50) <= 0.00001)

    def test_convert_to_percentage_basic(self):
        # Enter code here
        assert(abs(convert_to_percentage(5,10)-50) <= 0.0001)
        assert(abs(convert_to_percentage(5,20)-25) <= 0.0001)


    def test_average_mark_normal(self):
        # Enter code here
        assert(abs(average_mark(60,70)-65) <= 0.00001)

    def test_average_mark_boundary(self):
        # Enter code here
        assert(average_mark(1,1) == 1)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
