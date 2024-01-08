"""
Lab 3 Prep

Some example to help you with lab 3.  

    
"""
import math
"""

From book 2.13 - Convert the book solution to function form

## question 11 solution ##
deg_c = int(input("What is the temperature in Celsius? "))
# formula to convert C to F is: (degrees Celcius) times (9/5) plus (32)
deg_f = deg_c * (9 / 5) + 32
print(deg_f)

"""

def convert_to_f(deg_c):
    return 0

"""
From book, 2.13  

Convert the following code to function

## question 3 solution ##

current_time_string = input("What is the current time (in hours)? ")
waiting_time_string = input("How many hours do you have to wait? ")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int

timeofday = hours % 24

print(timeofday)

"""

def alarm(current_hour, waiting_hour):    
    return 0
    


"""
From 2.13

Convert the following code to function.  For the result, simply return the final amount.

## question 7 solution ##

P = 10000
n = 12
r = 0.08

t = int(input("Compound for how many years? "))

final = P * ( ((1 + (r/n)) ** (n * t)) )

print ("The final amount after", t, "years is", final)

"""

def compound_interest(t):    
    return 0

"""
The stock market often report the current price as a percentage of the 
previous day's price.

For example, if the yesterday's price was 100 and today's price is 103, then
it reports the stock has gone up by 3%.

> price_percentage(100, 103)
'3.0%'
> price_percentage(100, 90)
'-10.0%'
"""

def price_percentage(yesterday_price, today_price):
    return 0

"""
Write a function that takes the radius and height of a right cylinder and return 
the volume

   V = PI * (r^2) * h
"""

def volume_of_cylinder(r, h):    
    # note: math.pi gives us the most accurate pi value python can give us
    return 0

"""

Let's say we have 2 assignments in a class, assignment 1 is out of 20 and assignment 2 is out of 40.
However, both assignments are worth the same amount.

For example, if I score 15 for assignment 1, and 20 for assignment 2, my score for assignment 1 is actaully higher.

Write a function below that takes as input the 2 assignment marks, and return the higher mark in percentage.

Below are some examples of how this function would run in the console:

Test Case 1: assignment 1 has a higher mark and the score is 75% (15/20)
> better_mark(15, 20)
75.0

Test Case 2: assignment 2 has a higher mark and the score is 87.5% (35/40)
> better_mark(15, 35)
87.5

Test Case 3: assignment 3 has a higher mark and the score is 75% (30/40)
> better_mark(10, 30)
75.0

"""
def better_mark(assignment1_mark, assignment2_mark):
    return 0


"""

A local supermarket has a promotion where you get a discount if you buy 5 or more cans of chick peas.

The price for less than 5 cans of chick peas is 1.10 per can
The price for 5 or more cans of chick peas 0.9 per can

Write this function
"""

def calculate_price(num_cans):
    return 0
