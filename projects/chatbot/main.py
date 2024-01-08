
"""
This lab is inspired by the original "chatbot", ELIZA (https://en.wikipedia.org/wiki/ELIZA)
created by Joseph Weizenbaum.   

Also check out this video: https://youtu.be/RMK9AphfLco 

Many of the text files came directly from the ELIZA's language database.

A chatbot is able to carry on a conversation with a human.  It's essentially a 
function that takes a sentence as input and output another sentence as a response.

In this exercise, we will create an extrememly simple bot called echo, which really 
just echo the input sentence back to the user, with some slight modifications.

"""

import random

"""
Exercise 1:

Each line in the pronouns.txt file contains 2 words.  If the input word appears in the first
column, we replace it with the second word.

Given a word (string) as input, replace it with the corresponding word in the post_process_words.txt 
if it is found, otherwise output the original word.

> replace_word('am')
'are'
> replace_word('yourself')
'myself'

# this is the case where the word is not found, so we simply return the original word
> replace_word('circus') 
'circus'

You will need to make use of the technique in chapter 11.4 to process the file.

"""
def replace_pronoun(word):

    lang_data = open('pronouns.txt')

    new_word = word

    # Loop over every line in pronouns.txt
    # if the first word of the line matches the input word
    # return the second word on the line
    # If no match found, we return the original word    

    lang_data.close()
    return new_word

"""
Exercise 2:

For every word in a sentence, call replace_word then add a question mark '?' character at the end.

> process_sentence_pronouns('i am happy')
'you are happy?'
> process_sentence_pronouns('am i crazy')
'are you crazy?'

# in this case, nothing is changed
> process_sentence_pronouns('what is going on')
'what is going on?'

The technique you will need comes from chapter 9.14 - The Accumulator Pattern with Strings 

"""
def process_sentence_pronouns(sentence):
    new_sentence = ''

    # Use the accumulator pattern to create a new sentence with
    # every word replaced by the output of replace_pronoun
    
    return new_sentence

"""
Exercise 3:

Each line in the file synons.txt contains a list of words that are synonyms.  Complete the following
function so that give a word, if the word exist in any of the lines in the file, replace it with a 
random word from that line.  

If the input word doesn't appear in the synon_words.txt file, return the original input word.

> replace_synon('believe')
'wish'
> replace_synon('ok')
'ok'
"""
def replace_synon(word):

    lang_data = open('synons.txt')

    new_word = ''
    
    # very similar to replace_pronoun, but this time,
    # if word is found on the line, replace with a random 
    # word on the same line

    lang_data.close()
    return new_word

"""
Exercise 4:

Similar to post_process, call replace_word_synon for every word in the input sentence.

> process_sentence_synons('everyone like me')
'nobody like me'
> process_sentence_synons('i want to believe')
'i need to wish'

# this is the case where no words were replaced
> process_sentence_synons('i will survive')
'i will survive'
"""
def process_sentence_synons(sentence):
    new_sentence = ''

    # simliar to process_sentence_pronouns, but each
    # word of the sentence is replaced by the return
    # value from replace_synon
    
    return new_sentence.strip()    


"""
Exercise 5:

Noticed that for post_process() to work properly, the input needs to be all lower case
and without an '?' character at the end.

Complete the following pre_process function so that it return a lower case version of 
the input sentence, and remove all '?' character.

2 string functions will be very useful:

 - string.lower() - turns a string into lowercase (https://www.w3schools.com/python/ref_string_lower.asp)
 - string.replace('?','') - replace a character in a string with a different 
                            character (https://www.w3schools.com/python/ref_string_replace.asp)

                            
> pre_process('I want to believe?')
'i want to believe'
> pre_process('Everybody is kung fu fighting')
'everybody is kung fu fighting'

"""
def pre_process(sentence):
    
    # No loops here, simply return a lower case version
    # of the sentence, and remove all ? characters
    
    return sentence

"""
Exercise 6:

We are now ready to write our bot.  Here the bot function takes in a sentence and
perform 3 steps:

 - first, pre-process sentence so we turn all letters lowercase and remove question mark
 - second, we replace all synonms to make the sentence appear different
 - thrid, we replace all pronous as appropriate
 - return the resulting sentence

> bot('I want to believe')
'you need to think?'
> bot('I want to believe')
'you desire to belief?'
> bot('I want to believe')
'you desire to feel?'
> bot('I want to believe')
'you desire to wish?'

"""
def bot(sentence):

    # No loops - simply transform the input sentence by calling
    # pre_process(), then process_sentence_synons(), and finally process_sentence_pronouns()
    
    return ''

"""
Below you will find a main main function, allowing a user to interact with the chatbot 
in a more natural way. 

The following main function can only perform one single interaction.  Incorporate a while
loop similar to chapter 8.8 so that the program will keep asking for user input until 
the user enters the word 'quit'.  

> main()
Tell me your problem
You: I want to believe
Doctor: you want to wish?
You: Yes I wish the x-files will come back
Doctor: yes you believe the x-files will come back?
You: I totally believe it
Doctor: you totally think it?
You: quit
goodbye
> 

"""
def main():
    print('Tell me your problem')    
    q = input('You: ')
    
    response = bot(q)
    print('Doctor: '+response)
    
    print('goodbye')
    

