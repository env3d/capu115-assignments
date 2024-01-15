import unittest
from main import *

class UnitTests(unittest.TestCase):

    def test_gamer_novice(self):
        # Enter code here
        assert(gamer_type(90) == "novice")

    def test_gamer_pro(self):
        # Enter code here
        assert(gamer_type(90.01) == "pro")

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
