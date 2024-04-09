import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch

class UnitTests(unittest.TestCase):

    def test_exercise2_white(self):
        # Enter code here

        img = image.EmptyImage(10,10)
        for x in range(10):
            for y in range(10):
                img.setPixel(x, y, image.Pixel(128,128,128))

        with patch.object(image, 'Image', return_value=img):
            exercise2()

            for x in range(10):
                for y in range(10):
                    assert tuple(img.getPixel(x,y)) == (255,255,255)


    def test_exercise3(self):
        # Enter code here

        img = image.EmptyImage(10,10)
        for x in range(10):
            for y in range(10):
                img.setPixel(x, y, image.Pixel(100,100,100))

        with patch.object(image, 'Image', return_value=img):
            exercise3()

            for x in range(10):
                for y in range(10):
                    assert tuple(img.getPixel(x,y)) == (50,50,50)


    def test_exercise1(self):
        # Enter code here

        img = image.EmptyImage(10,10)
        for x in range(10):
            for y in range(10):
                img.setPixel(x, y, image.Pixel(127,127,127))

        with patch.object(image, 'EmptyImage', return_value=img):
            exercise1()

            for x in range(10):
                for y in range(10):
                    if y < 5:
                        assert tuple(img.getPixel(x,y)) == (0,0,0), img.getPixel(x, y)
                    else:
                        assert tuple(img.getPixel(x,y)) == (255,255,255), img.getPixel(x, y)


    def test_exercise2_black(self):
        # Enter code here

        img = image.EmptyImage(10,10)
        for x in range(10):
            for y in range(10):
                img.setPixel(x, y, image.Pixel(127,127,127))

        with patch.object(image, 'Image', return_value=img):
            exercise2()

            for x in range(10):
                for y in range(10):
                    assert tuple(img.getPixel(x,y)) == (0,0,0)


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
