"""
Lab 2

Coding Functions

Objectives

    Practice coding simple Python functions,
    Practice using functions,
    Practice testing functions.

Partner: _______

"""

import math

"""
Exercise 1

1 US dollar is around 1.29 Canadian dollars.
Write a function that takes American dollars as input 
and return the  Canadian dollars equivalent 
"""
def convert_dollars(american):
    return american * 1.29


"""
Exercise 2

Write a function that converts the mileage of a vehicle in l/100km into mpg. We know that

1 l/100km  = 235.215 mpg

HINT: Use the google unit conveter to help: https://www.google.com/search?q=lper+100+km+into+mpg
      The equation is shown in the google search.
"""
def convert_mileage(liters_per_100km):
    return 0


"""
Exercise 3

The length of an organism is typically strongly correlated with its body mass using the following formula:

mass = a * length^b (note: ^ means "to the power of")

where the mass is measured in kilograms and length in meters and where the parameters a and b vary among groups.

In 2001 for Theropoda researcher Frank Seebacher estimated as follows:

a = 0.73 and b = 3.63 

(http://www.jstor.org/stable/4524171?seq=1#page_scan_tab_contents). 
His research allows us to estimate a weight of a member of Theropoda family 
from the length of its skeleton using the above formula.

Write a function that takes the length of a member of of Theropoda as input and returns its estimated weight.

A test case would be a specimen of a Spinosaurus that is 16 m long based on it’s reassembled skeleton. Calculate its weight using the above formula by hand and test your function to see that it gives the same result.
"""
def estimate_theropoda(length):
    return 0

"""
Exercise 4

Create a more general version of the function from the last exercise that estimates the weight of an dinosaur 
but also takes the values of a and b as input. Use this new function to estimate the mass of a 
Sauropoda (a = 214.44, b = 1.46) that is 26 m long. Use your function to estimate the weight of 
Spinosaurus from the previous exercise.
"""
def estimate_dino(a, b, length):
    return 0

"""
Exercise 5

In a company, fixed assets such as computers lose their value over time and this charge is called depreciation.  The way to account for this in the company books is called declining balance depreciation. Each year the value of an asset depreciates by a fixed percentage. For example, assume that a piece of equipment is bought for $10, 000 and it depreciates at 10% a year. The first year depreciation of the item is: $10,000 * 0.10 = $1000. The item is now valued at $9000.

Write a function that takes the current value of an item (in $) and the depreciation rate as input and computes the depreciated value after one year.
"""
def depreciate_one_year(initial_price):
    return 0

"""
Exercise 6 (Challenge)

Continuing from the last exercise, for an item that costs $10,000 an depreciates at 10% a year, the second year depreciation is: $9,000 * 0.10=$900. After two years the item is now valued at $8,100. This process can go on for any number of years.

Write a function that takes the value of the item, depreciation and number of years as inputs and calculates the value of the item at the end of the time period.

Check out this link for the necessary formula: http://ilovemaths.com/3depreciation.asp 
"""
def depreciate_multiple_years(initial_price, years):
    return 0

