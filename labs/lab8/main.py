"""
Objectives

 - Practice using strings and string functions and methods,
 - Practice writing functions,
 - Practice functional decomposition.

Problem Description

Pig Latin is a language game in which words are transformed to conceal their meaning from others not familiar with the rules.  Look at http://en.wikipedia.org/wiki/Pig_Latin for more information.

To translate from English to Pig Latin do the following:

For words that begin with consonant sounds, the initial consonant or consonant cluster is moved to the end of the word, and "ay" is added. For example:

  "pig" → "igpay"
  "banana" → "ananabay"
  "trash" → "ashtray“
  "happy" → "appyhay"
  "duck" → "uckday"
  "glove" → "oveglay“
  “scheme” → “emeschay“
  
For words which begin with vowels, "way"  is added to the end of the word. For example

"egg" → "eggway"
"inbox" → "inboxway"
"eight" → "eightway

"""

"""
Exercise 1

Assume the input word starts starts with a vowel as input, translate that word into pig-latin.

You can assume all input are lower case
"""
def translateVowel(word):
    return ''

"""
Exercise 2

Assume the input word starts with a consonant, return the pig-latin version of the word

You can assume all input are lower case.

Hint: you will need to figure out location of the first vowel.  Below is some code that will help with that task:

    i = 0
    while word[i] not in 'aeiou':
        i = i + 1

    # at this point, i is the index of first vowel

"""
def translateConsonant(word):
    return ''
    
"""
Exercise 3

Given any word as input, return the pig-latin version of the word.
This function will use a "if" statement to determine which of 
the above functions to call.

You can assume all input are lower case
"""
def translateWord(word):
    return ''

"""
Exercise 4

Using the technique from 9.14 (The Accumulator Pattern with Strings), write a function
that translates a sentence into pig latin.  Your algorithm will need to do the following:

 - loop over every word of the sentence
 - translate each word into pig latin
 - combine the words into the translated sentence
 - return the translated sentence

To split a sentence into a list of words, you can do the following: 

    words = sentence.split()

Then you can process the words like in the following loop that just prints them out:

    for word in words:    
         print(word)

You can assume that there are no punctuations and sentences are all lower case 
"""
def translate(sentence):
    return ''
