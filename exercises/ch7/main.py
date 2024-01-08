
"""

Lab 7: Practice writing IF statements

"""

import turtle

"""
Exercise 1:

Modify the answer to Chapter 7.10 Ex 3 to use the 
following breakdown for grades:

Mark	   Grade

>= 80      A
[70-80)    B
[60-70)    C
[50-60)    D
< 50       F

"""

def grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

"""
Exercise 2:

Complete chapter 7.10 exercise 4 by modifying the
drawBarChart() function.

You can see a running version at https://youtu.be/HfLTlGm3zq8 

"""
def drawBar(t, height):
    """ 
    From the text, DO NOT MODIFY
    Get turtle t to draw one bar of a particlar height.    
    """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def drawBarChart(t, xs):
    """
    This function can be called from the console as follows:

    t = turtle.Turtle()
    drawBarChart(t, [50, 100, 75])

    Your job is to modify this function so that the bar for any value of 200 
    or more is filled with red, values between [100 and 200) are filled yellow, 
    and bars representing values less than 100 are filled green.

    NOTE: to pass the automated tests, you MUST use the color() method to change 
    the turtle's color, and the color must be in lower case.
    """
    for a in xs:
        if a >= 200:
            t.color('red')
        elif a >= 100:
            t.color('yellow')
        else:
            t.color('green')
            
        drawBar(t, a)



"""
Exercise 3:

From chapter 7.10 exercise 12


Write a function that takes as input a year (in number) and
return True if it is a leap year, false otherwise.

How to calculate leap year:

ALL 3 of the following criteria must be taken into account to identify leap years:

- The year is evenly divisible by 4;
- If the year can be evenly divided by 100, it is NOT a leap year, unless;
- The year is also evenly divisible by 400. Then it is a leap year.

Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.

You can check your answer against this leap year calculator: 
    https://www.omnicalculator.com/everyday-life/leap-year

"""
def isLeapYear(year):
    return False

        

