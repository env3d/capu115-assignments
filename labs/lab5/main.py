"""
    Lab 5: Draw Alkane chains (organic chem. visualization)
           (starter project by J. Madar, based on original idea from T. Dakic and J. Fall)    

    Objectives 

        Practice using the turtle class methods,
        Practice with loops,
        Enhancing problem solving skills.

    Project Description

        This lab is based on organic chemistry.  Please read the project
        description at, which includes sample output of what is expected:
        
        https://docs.google.com/document/d/1_8ncRWWqiHGCR0YNAhkyIS2T5SkgSiFMJNdZbrC8r-s/edit?usp=sharing

"""

import turtle

# The following variables are availble for all defined functions.  
# These are values that can be used in place with using numbers
# It makes your code more readable

# font_size changes the default size of your letters
font_size = 20

# each letter has an invisble box around it, with
# specific height and width in pixels
font_height = font_size
font_width = font_size * (1 - 0.39)

# DO NOT MODIFY:
# The draw_letter function, is provided for you so you can 
# easily draw letters on the screen using turtle
def draw_letter(turtle, letter):
    """
    This function takes a turtle and draw a letter at the current
    turtle location, where the center of the letter is
    at the turtle's tip
    """
    height = font_size
    turtle.setx(turtle.xcor() - (font_width / 2))
    turtle.sety(turtle.ycor() - (height / 2))
    turtle.write(letter, font=('Courier', font_size))
    turtle.setx(turtle.xcor() + (font_width / 2))
    turtle.sety(turtle.ycor() + (height / 2))


"""
Exercise 1:

Write a function to draw CH(2) on screen.

Please note that this function takes a turtle as input, 
so you'll have to call it from the console as follows:

> steve = turtle.Turtle()
> draw_carbon(steve)
"""

def draw_carbon(t):
    pass
    
"""
Exercise 2:

Draw a series of carbons, but without the first and last H

"""
def draw_carbons(t, num_carbons):
    pass

"""
Exercise 3:

Draw the carbon chains with all the H's present. 
i.e. the first and last carbon have 3 H's and the
middle of the chain with only have 2 H's

Please note that this function does not take in a turtle 
as input, so we will need to create a turtle inside the function.

We call this function the "entry point" of our carbon drawing
software.  
"""
def draw_carbon_chain(num_carbons):
    t = turtle.Turtle()
    pass

