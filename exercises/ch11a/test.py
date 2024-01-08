import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch, mock_open

class UnitTests(unittest.TestCase):

    def test_reformat_data(self):
        # Enter code here
        # Enter code here
        data = "1850 1 2\n1950 0 2\n2000 -1 2"
        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            reformat_data()
            assert len([c for c in mock_file.mock_calls if 'write' in str(c)]) == 3

    def test_calculage_avg_temp_range(self):
        # Enter code here
        # Enter code here
        data = "1850 1 2\n1950 0 2\n2000 -1 2"
        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            assert calculate_avg_temp_range(1949, 1951) == 0

    def test_calculate_avg_temp(self):
        # Enter code here
        data = "1850 1 2\n1950 0 2\n2000 -1 2"
        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            assert calculate_avg_temp() == 0

    def test_calculate_emission_range(self):
        # Enter code here
        data = "1850 1 2\n1950 0 2\n2000 -1 2"
        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            assert calculate_emission_range(1850,1960) == 4

    def test_calculate_total_emission(self):
        # Enter code here
        data = "1850 1 2\n1950 0 2\n2000 -1 2"
        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            assert calculate_total_emission() == 6


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
