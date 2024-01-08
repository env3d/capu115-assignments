import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_translate_vowel(self):
        # Enter code here
        assert(translateVowel('abcde') == 'abcdeway')
        assert(translateVowel('inbox') == 'inboxway')
        assert(translateVowel('egg') == 'eggway')

    def test_translate_consonant(self):
        # Enter code here
        pig_map = {
          "pig" : "igpay",
          "banana" : "ananabay",
          "trash" :  "ashtray",
          "happy" : "appyhay",
          "duck" : "uckday",
          "glove" : "oveglay",
          "scheme" : "emeschay"
        }

        for k,v in pig_map.items():
            assert translateConsonant(k) == v


    def test_translate_word(self):
        # Enter code here
        pig_map = {
          "pig" : "igpay",
          "banana" : "ananabay",
          "trash" :  "ashtray",
          "happy" : "appyhay",
          "duck" : "uckday",
          "glove" : "oveglay",
          "scheme" : "emeschay",
          "egg" : "eggway",
          "inbox" : "inboxway",
          "eight" : "eightway"
        }

        for k,v in pig_map.items():
            assert translateWord(k) == v

    def test_translate(self):
        # Enter code

        assert translate('hello world') == 'ellohay orldway'
        assert translate('what is your name') == 'atwhay isway ouryay amenay'
        assert translate('london bridge is falling down') == 'ondonlay idgebray isway allingfay ownday'

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner().run(s)
