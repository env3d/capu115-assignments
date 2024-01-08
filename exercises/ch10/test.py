import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_kids_with_candies(self):
        # Enter code here
        assert kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True]
        assert kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False]
        assert kidsWithCandies([12,1,12], 10) == [True,False,True]

    def test_maximum_wealth(self):
        # Enter code here
        assert maximumWealth([[1,2,3],[3,2,1]]) == 6
        assert maximumWealth([[1,5],[7,3],[3,5]]) == 10
        assert maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17


    def test_most_words_found(self):
        # Enter code here
        assert mostWordsFound([])  == 0
        assert mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])  == 6
        assert mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3

    def test_running_sum(self):
        # Enter code here
        assert runningSum([1,2,3,4]) == [1,3,6,10]
        assert runningSum([1,1,1,1,1]) == [1,2,3,4,5]
        assert runningSum([3,1,2,10,1]) == [3,4,6,16,17]

    def test_get_concatenation(self):
        # Enter code here
        assert getConcatenation([]) == []
        assert getConcatenation([1,2,3]) == [1,2,3,1,2,3]


    def test_count_length(self):
        # Enter code here
        assert count_length([]) == 0
        assert count_length(['a','b','c','e']) == 0
        assert count_length(['aaaa','bbbbb','ccccc','eee']) == 2

    def test_sum_of_squares(self):
        # Enter code here
        assert sum_of_squares([]) == 0
        assert sum_of_squares([1,1,1,1,1]) == 5
        assert sum_of_squares([1,2,3,4,5]) == 55

    def test_find_max(self):
        # Enter code here
        assert find_max([]) == None
        assert find_max([1,2,3,4,5]) == 5
        assert find_max([5, 6, 7, 81, 44, 22]) == 81


    def test_average(self):
        # Enter code here
        assert average([]) == 0
        assert average([1,1,1,1,1]) == 1
        assert average([1,2,3,4,5]) == 3

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
