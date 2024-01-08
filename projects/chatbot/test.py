import unittest
from main import *

# Add imports here
from unittest.mock import MagicMock, patch

class UnitTests(unittest.TestCase):

    def test_replace_pronoun(self):
        # Enter code here
        '''
        am are
        your my
        me you
        myself yourself
        yourself myself
        i you
        you I
        my your
        i'm you're
        '''
        assert(replace_pronoun('i') == 'you')
        assert(replace_pronoun('myself') == 'yourself')
        assert(replace_pronoun('hello') == 'hello')

    def test_process_sentence_pronouns(self):
        # Enter code here
        assert(process_sentence_pronouns('i am happy') == 'you are happy?')
        assert(process_sentence_pronouns('am i crazy') == 'are you crazy?')
        assert(process_sentence_pronouns('what is going on') == 'what is going on?')


    def test_replace_synon(self):
        # Enter code here
        assert(replace_synon('believe') in ['belief', 'feel', 'think', 'believe', 'wish'])
        assert(replace_synon('ok') == 'ok')

    def test_process_sentence_synon(self):
        # Enter code here

        with patch('main.replace_synon', return_value='a') as synon_mock:
            assert(process_sentence_synons('i want to believe') == 'a a a a')

    def test_pre_process(self):
        # Enter code here
        assert(pre_process('I want to believe?') == 'i want to believe')
        assert(pre_process('Everybody is kung fu fighting') == 'everybody is kung fu fighting')


    def test_bot(self):
        # Enter code here
        with patch('main.pre_process') as pre:
            with patch('main.process_sentence_synons') as syn:
                with patch('main.process_sentence_pronouns', return_value='a') as pro:
                    r = bot('a b c d e')
                    assert(r=='a'), 'Must return a sentence'
                    assert(pre.called)
                    assert(pro.called)
                    assert(syn.called)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
