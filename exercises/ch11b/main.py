"""
Dataset from IMDb

name.basics.tsv, but only contain actors

Refer to https://www.imdb.com/interfaces/ for details
"""

"""
Return the first 10 names from the file namne.basics.tsv
"""

def get_first_10_names():
    infile = open('name.basics.tsv')

    names = []

    # The names list is used to store the actors names 
    # in the accumulator pattern
    
    infile.close()
    return names

"""
Find actor and return the entire line from file, if not found return empty string ('')
"""    
def find_actor(actor_name):
    infile = open('name.basics.tsv')

    actor = ''

    # Use the accumulator pattern to locate the actor line
            
    infile.close()
    return actor


"""
Count the number of actors born after a certain year
"""
def count_actors_born_after(year):
    infile = open('name.basics.tsv')

    count = 0

    # use the accumulator pattern with an IF statement
    
    infile.close()
    return count
    
def count_dead_actors():
    infile = open('name.basics.tsv')

    dead = 0

    # HINT: For an actor to be dead, field #3 must contain a valid year
    # Alive actors have the string \\N in field #3
    
    infile.close()
    return dead

"""
Return the name of the youngest actor
"""
def find_youngest_actor():
    infile = open('name.basics.tsv')

    actor = ''
    
    # This one is challenging.  Youngest actor means the birth year is the latest.
    
    infile.close()
    return actor
