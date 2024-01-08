"""
Original dataset from https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset 

This is an exercise on a field called data analysis, where we use python to process and
gather various statistics on a text file containing text messages that is marked
either SPAM or HAM (HAM meaning not spam)

The spam.txt file contains real text messages from various sources.  The first word
of each line specifies if the message is either "spam" or "ham" (once again, 
"ham" means it's a text message between real people).

All the questions asked you to analyze the spam.txt file, but during development, you 
may want to use spam_mini.txt so you can test your functions better.
"""

"""
Exercise 1: open the spam.txt file and return a count of the number of spam messages included in the dataset
            HINT: simply count sentences that starts with the word "spam"
"""
def count_spam():
    f = open('spam.txt')
    spam_count = 0
    # use the accumulator pattern here 
    return spam_count


"""
Exercise 2: Similar to exercise 12.7.3 from the textbook, return a dictionary of all words and the corresponding 
            count in all spam messages.

            For instance, if we look at the following spam messages:
                "Free prize!"
                "Urgent! claim your free prize!"
                "Free bluetooth"

            The calling the function would return:
            {'free': 3, 'prize':2, 'urgent': 1, 'bluetooth': 1, 'claim': 1, 'your': 1}
"""
def get_spam_dictionary():
    # create the words dictionary to hold the word count
    words = {}
    f = open('spam.txt')
    # make sure you checkout exercise 12.7.3 from the textbook 
    f.close()                    
    return words


"""
Exercise 3: Repeat exercise 2, but create a word dictionary for ham messages instead of spam messages
"""
def get_ham_dictionary():
    words = {}
    f = open('spam.txt')

    # the solution here is very similar to exercise 2
    
    f.close()                    
    return words


"""
Exercise 4: Return only the words that are unique to the spam dictionary.  
"""
def get_unique_spam():
    ham = get_ham_dictionary()
    spam = get_spam_dictionary()

    # we need to delete all the ham entries from the spam entry
    
    return {}

"""
Exercise 5: Return unique spam words that are greater than a certain frequencies.  
            For instances, if the unique spam words are: 
            {'free': 3, 'prize':2, 'urgent': 1, 'bluetooth': 1, 'claim': 1, 'your': 1}
            Then we would have the following interaction in the conosle:

            > get_frequent_words(2)
            ['free', 'prize']

            After you have created this function, can you tell me what are the words that
            exist in over 10% of all spam messages?
"""
def get_frequent_words(gt):
    result = []

    # use the acculmulator pattern here
    
    return result

