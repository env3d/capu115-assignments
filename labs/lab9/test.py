import unittest
from main import *

# Add imports here
from unittest.mock import patch

class UnitTests(unittest.TestCase):

    def test_sentiment_return_list(self):
        # Enter code here
        l = get_sentiments(['very good!','excellent!','perfect!'])
        # [0.54, 0.6114, 0.6114]
        assert(type(l) is list)



    def test_sentiment_values(self):
        # Enter code here
        l = get_sentiments(['very good!','excellent!','perfect!'])
        # [0.54, 0.6114, 0.6114]
        for i in l:
            assert(i > 0.5 and i < 0.65)

    def test_max_score(self):
        # Enter code here
        score = get_max_score(['very good!','excellent!','perfect!'])
        # [0.54, 0.6114, 0.6114]
        assert(score > 0.6 and score < 0.62)

    def test_min_score(self):
        # Enter code here
        score = get_min_score(['very good!','excellent!','perfect!'])
        # [0.54, 0.6114, 0.6114]
        assert score > 0.53 and score < 0.55, score

    def test_positive_only(self):
        # Enter code here
        l = positive_only(['very good!','excellent!','perfect!'])
        # [0.54, 0.6114, 0.6114]
        assert(len(l) == 3)
        l = positive_only(['very bad!','worst!','terrible!'])  # [0.54, 0.6114, 0.6114]
        assert(len(l) == 0)



    def test_negative_only(self):
        # Enter code here
        # Enter code here
        l = negative_only(['very good!','excellent!','perfect!'])
        # [0.54, 0.6114, 0.6114]
        assert(len(l) == 0)
        l = negative_only(['very bad!','worst!','terrible!'])
        # [-0.623, -0.6588, -0.5255]
        assert(len(l) > 0)


    def test_most_positive(self):
        # Enter code here

        with patch('main.get_reddit_news', return_value=['very good!','excellent!','very bad!','worst!','terrible!']) as mock_reddit:


            n = get_most_positive_news()
            # [0.54, 0.6114, 0.6114, -0.623, -0.6588, -0.5255]
            assert(mock_reddit.called)
            assert n == 'excellent!'




    def test_most_negative(self):
        # Enter code here
        with patch('main.get_reddit_news', return_value=['very good!','excellent!','very bad!','worst!','terrible!']) as mock_reddit:

            n = get_most_negative_news()
            # [0.54, 0.6114, -0.623, -0.6588, -0.5255]
            assert (mock_reddit.called)
            assert n == 'worst!'


if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
