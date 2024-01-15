import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch

class UnitTests(unittest.TestCase):
    def test_random_one_color(self):
        # Enter code here
        mockImage = MagicMock()
        mockImage.setPixel = MagicMock()
        mockImage.getHeight = MagicMock(return_value=6)
        mockImage.getWidth = MagicMock(return_value=6)

        mockImage.set_pixel = mockImage.setPixel
        mockImage.get_height = mockImage.getHeight
        mockImage.get_width = mockImage.getWidth

        with patch.object(image, 'EmptyImage', return_value=mockImage):
            with patch.object(random, 'random', return_value=1) as rand:
                createRandomNoise(6,6)
                assert rand.called, "random.random() must be called somewhere in your code"
                prev_pixel = mockImage.setPixel.mock_calls[0][1][2]
                for i in range(len(mockImage.setPixel.mock_calls)):
                    assert(tuple(prev_pixel) == tuple(mockImage.setPixel.mock_calls[i][1][2]))
                    prev_pixel = mockImage.setPixel.mock_calls[i][1][2]


    def test_alternate_lines(self):
        # Enter code here
        mockImage = MagicMock()
        mockImage.setPixel = MagicMock()
        mockImage.getHeight = MagicMock(return_value=6)
        mockImage.getWidth = MagicMock(return_value=6)

        mockImage.set_pixel = mockImage.setPixel
        mockImage.get_height = mockImage.getHeight
        mockImage.get_width = mockImage.getWidth

        with patch.object(image, 'EmptyImage', return_value=mockImage):
            createAlternateLines(6,6)

            assert (mockImage.setPixel.called)
            # should have 5 calls to setPixel white
            white_pixels = [ x[1][2] for x in mockImage.setPixel.mock_calls if tuple(x[1][2]) == (255, 255, 255)]

            black_pixels = [ x[1][2] for x in mockImage.setPixel.mock_calls if tuple(x[1][2]) == (0, 0, 0)]

            assert (len(white_pixels) == len(black_pixels))

            #assert False, white_pixels

    def test_white_line(self):
        # Enter code here
        mockImage = MagicMock()
        mockImage.setPixel = MagicMock()
        mockImage.getHeight = MagicMock(return_value=6)
        mockImage.getWidth = MagicMock(return_value=6)

        mockImage.set_pixel = mockImage.setPixel
        mockImage.get_height = mockImage.getHeight
        mockImage.get_width = mockImage.getWidth

        with patch.object(image, 'EmptyImage', return_value=mockImage):
            createWhiteLine(6,6)

            # should have 5 calls to setPixel white
            white_pixels = [ x[1][2] for x in mockImage.setPixel.mock_calls if tuple(x[1][2]) == (255, 255, 255)]

            assert (len(white_pixels) == 6)

            #assert False, white_pixels

    def test_decode_image(self):
        # Enter code here
        mockImage = MagicMock()
        mockImage.setPixel = MagicMock()
        mockImage.getHeight = MagicMock(return_value=10)
        mockImage.getWidth = MagicMock(return_value=10)

        mockImage.set_pixel = mockImage.setPixel
        mockImage.get_height = mockImage.getHeight
        mockImage.get_width = mockImage.getWidth

        full_red_even = image.EmptyImage(10,10)
        for x in range(10):
            for y in range(10):
                full_red_even.setPixel(x, y, image.Pixel(254, 0, 0))

        full_red_odd = image.EmptyImage(10,10)
        for x in range(10):
            for y in range(10):
                full_red_odd.setPixel(x, y, image.Pixel(255, 0, 0))

        with patch.object(image, 'EmptyImage', return_value=mockImage) as EmptyImage:

            with patch.object(image, 'FileImage', return_value=full_red_even) as FileImage:
                with patch.object(image, 'Image', return_value=full_red_even) as MyImage:

                    decodeImage()
                    assert FileImage.called or MyImage.called, "Must retrieve encoded_image.gif"
                    assert EmptyImage.called, "Must create a new image to store the decoded message"

            with patch.object(image, 'FileImage', return_value=full_red_odd) as FileImage:
                with patch.object(image, 'Image', return_value=full_red_odd) as MyImage:

                    decodeImage()
                    assert FileImage.called or MyImage.called, "Must retrieve encoded_image.gif"
                    assert EmptyImage.called, "Must create a new image to store the decoded message"

            num_black = len([x for x in mockImage.setPixel.mock_calls if tuple(x[1][2]) == (0,0,0)])
            num_white = len([x for x in mockImage.setPixel.mock_calls if tuple(x[1][2]) == (255,255,255)])
            num_red = len([x for x in mockImage.setPixel.mock_calls if tuple(x[1][2]) == (255,0,0)])


            assert (num_black > 0 and (num_white > 0 or num_red > 0))
            assert (num_black == num_white or num_black == num_red)


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
