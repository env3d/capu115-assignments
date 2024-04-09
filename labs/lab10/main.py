"""

Challenge 10b: Lists

Learning Objectives:

 - Practice using lists and and list indexing,
 - Practice using loops,
 - Practice writing functions.


Background

In recent years, AI advances have allowed computers to perform functions that used to be the exclusive domain of 
human beings.  One of these fields is for computers to understand natural languages.

Understanding may be a bit of an overstatement, as you will see, the AI system is simply providing us a
function where the input is a sentence, and it returns the sentence's sentiment as a number.

Your job is to use this AI to analyze live newsfeeds from reddit, a popular news forum.

I have provided you with the following 2 functions:

    get_sentiment(sentence) - given a sentence (string), it returns a number indiciating the sentiment (or emotion) of the 
    sentence.  Note the following interaction:

    > get_sentiment('this is going to be a great day!')
    0.6588
    > get_sentiment('i hate rainy mornings!')
    -0.6476

    The number returned is of float type and in the range of [-1.0, 1.0].  The higher the number, the more positive the sentence,
    and vice-versa/

    get_reddit_news() - retrieves a list of news titles from reddit's 'worldnews' forum.  
    

You will need to use these functions to complete the exercises.  Pretty much all exercises require you to loop over a list 
of itmes using a for loop and process each item in the list.

"""


from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from urllib.request import urlopen, Request
import json

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


##### You will use the following functions to complete the exercises #######

"""
The get_sentiment() function returns a number between -1 and 1 for a given string (sentence).  
The higher the number, the more positive the sentiment is.  
"""


def get_sentiment(sentence):     
    return sid.polarity_scores(sentence)['compound']


"""
The get_reddit_news function return a list of current world news titles from reddit's worldnews 
"""

def get_reddit_news(url = 'https://www.reddit.com/r/worldnews/.json'):
    my_socket = urlopen(Request(url, headers={'User-Agent':'abcde'}))
    dta = my_socket.read()
    reddit_data = json.loads(dta)    
    titles = [x['data']['title'] for x in reddit_data['data']['children']]
    return titles


####### Start of the exercises #########

"""
Exercise 1:

Given a list of sentences as input, return a list of corresponding sentiments

Here is how I would use the function:
> get_sentiments(['good day!','terrible day'])
[0.4926, -0.4767]


"""
def get_sentiments(list_of_sentences):
    sentiment_list = []

    # use the accumulator patern here as per Chatper 10.22    
    
    return sentiment_list


"""
Exercise 2:

Given a list of sentences as input, return the maximum (most positive) score

Here is how I would use the function:

> get_max_score(['good day!','terrible day'])
0.4926

"""

def get_max_score(list_of_sentences):
    # first we get a list of scores from previous exercise
    scores = get_sentiments(list_of_sentences)

    # now we find the max score
    max_score = 0

    # use the acculmulator as per 10.18.1
    
    return max_score

"""
Exercise 3:

Given a list of sentences as input, return the minimum (most negative) score

Here is how I would use the function:

>get_min_score(['good day!','terrible day'])
-0.4767

"""
def get_min_score(list_of_sentences):
    scores = get_sentiments(list_of_sentences)
    min_score = 1

    # same as previous exercise, but find min instead of max

    return min_score

"""
Exercise 4:

Given is list of sentences, return a list of only positive items.

i.e.
> positive_only(['good day!','terrible day','I love today'])
['good day!', 'I love today']

"""
def positive_only(list_of_sentences):
    positive_items = []
    
    # use the acculmulator pattern.  
    # for every sentence, we first find out the numerical
    # sentiment value.  If positive, we add it to 
    # the return list
    
    return positive_items

"""
Exercise 5:

Given is list of sentences, return a list of only negative items.

i.e.
> negative_only(['good day!','terrible day','I love today','I feel sad'])
['terrible day', 'I feel sad']

"""
def negative_only(list_of_sentences):
    negative_items = []

    # same as previous but only accumulate negative items
    
    return negative_items


"""
Exercise 6:

Return the MOST POSITIVE news from reddit right now (using the get_reddit_news() function)

> get_most_positive_news()
'Armenia’s Central Bank improves GDP growth forecast from 1.6 to 13% due to mass influx of ‘talented and well-educated’ Russians into the country'

"""
def get_most_positive_news():
    news_items = get_reddit_news()    
    max_score = get_max_score(news_items)

    # search each news item from reddit, and
    # return the item that matches the max_score

    return ''

"""
Exercise 7:

Return the MOST NEGATIVE news from reddit right now (using the get_reddit_news() function)

> get_most_negative_news()
'Ukraine Sends Stark Warning to Belarus Against Joining War'

"""
def get_most_negative_news():
    news_items = get_reddit_news()
    min_score = get_min_score(news_items)

    # same as previous but return the item with most
    # negative score

    return ''
        
