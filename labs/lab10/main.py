"""
Lab 10

This lab is all about working with files.  The gerenal pattern for working
with files to use loops and process a file one line at a time.

The typical reason why we work with files is because these files are too big or
change all the time so the data cannot be included inside our program.  

For this lab We are going to use data from IMDb (Internet Movie Database).  I
have prepared 2 data files for you (only contains data from 2020-present):

 - title.basics.tsv.gz - Contains the following fields for titles:

    tconst (string) - alphanumeric unique identifier of the title
    titleType (string) – the type/format of the title (This file only contain movie type)
    primaryTitle (string) – the more popular title / the title used by the filmmakers 
                            on promotional materials at the point of release
    originalTitle (string) - original title, in the original language
    isAdult (boolean) - 0: non-adult title; 1: adult title
    startYear (YYYY) – represents the release year of a title.
    endYear (YYYY) – TV Series end year. \N for all other title types
    runtimeMinutes – primary runtime of the title, in minutes
    genres (string array) – includes up to three genres associated with the title
    
 - title.ratings.tsv.gz – Contains the IMDb rating and votes information for titles
 
    tconst (string) - alphanumeric unique identifier of the title
    averageRating – weighted average of all the individual user ratings
    numVotes - number of votes the title has received

These files are similar to chapter 11.4 of the textbook in that you 
can use line.split() to separate each line into fields.

The details of these files can be found at https://www.imdb.com/interfaces/

"""

"""
Exercise 1

Unlike a list, you cannot simply use the len() function find 
out how many lines a file has.  You have to actually loop over 
a file an use the accumulator pattern to count the lines.

Using the technique described in 
https://runestone.academy/ns/books/published/thinkcspy/Files/Iteratingoverlinesinafile.html
complete the following function so it returns the number of 
lines in the file title.basics.tsv
"""
def count_titles():
    f = open('title.basics.tsv')    
    

    f.close()
    return 0


"""
Exercise 2

In the file title.basics.tsv, the 5th field contains a string indicating
if the title belongs in the "adult" category.  Complete the following 
function which returns the number of adult titles in title.basics.tsv.

You will need to first split each line into fields (as shown in 11.4), 
and then use an IF statement inside the loop to selectively count the titles.

"""
def count_adult_titles():
    f = open('title.basics.tsv')
    

    
    f.close()
    return 0

"""
Exercise 3

Similar to the previous exercise, but count the number of "Romance" titles.

Note that the genre is stored in the 9th field, but since a movie can have mutiple
genres, it is a string separated by commas.

For example, the following is the entry for 'The Hunger Games':
tt1392170 movie The_Hunger_Games The_Hunger_Games 0 2012 \N 142 Action,Adventure,Sci-Fi

It belongs to 3 genres: Action, Adventure, and Sci-Fi

"""
def count_romance_titles():
    f = open('title.basics.tsv')

    f.close()
    return 0

"""
Exercise 4

Give a movie_title as input, output its title id (field #1)
If the title is not found, return the empty string ''.

Note that titles are case sentitive and words are separated by underscore (_)

> find_title_id('The_Hunger_Games')
'tt1392170'
> find_title_id('The_Avengers')
'tt0848228'
> find_title_id('avengers')
''

"""
def find_title_id(movie_title):
    f = open('title.basics.tsv')

    f.close()
    return ''

    
"""
Exercise 5

Give a movie_title as input, output its IMDB rating
If the title is not found, return -1.

Note that titles are case sentitive and words are separated by underscore (_)

> get_rating('The_Hunger_Games')
7.2
> get_rating('The_Avengers')
8.0
> get_rating('avengers')
-1.0 


"""
def get_rating(movie_title):

    f = open('title.ratings.tsv')

            
    f.close()
    return -1

