"""
    Lab 6: Analyze & visualize bead pendants
    
    Author:  <your name here>
            (starter project by J.Madar and J. Fall, based on original idea from T. Dakic)
    Date:  <today>

    The running version of this lab can be found at: https://youtu.be/tbDAkY8nEOM 

    If you want an additional challenge (no additional points, just for interest), try to 
    do this instead: https://youtu.be/BAz6C-3sBrA 
    
"""
import turtle

# Data Definitions
BEAD_SIZE = 30                   # Size of one bead in the pendant
BEAD_SPACING = BEAD_SIZE * 1.0   # Space between bead centres


"""

Just a basic example how to use the dot() function of turtle
Call it from the console using the following:

t = turtle.Turtle()
basic_example(t)

"""
def basic_example(t):
    t.dot(BEAD_SIZE)
    t.forward(BEAD_SPACING)
    t.dot(BEAD_SIZE)

"""
Exercise 1:

Draw a row of beads.  This function takes a turtle
and a number of beads and use the dot() function of turtle to 
draw a series of dots on screen.

To test this, you will need to first create a turtle
on the console, like so:

t = turtle.Turtle()
draw_row(t, 5) # draws a 5 dots in a row

"""
def draw_row(t, num_beads):
    pass

"""
Exercise 2:

Draw a triangle of num_rows with a series of dots given a turlte and
a number of rows.  The first row will have 1 dot and the second 
row will have 2 dots, etc.  Like this:

draw_triangle(t, 5) will produce output similar to the 
following:

*
**
***
****
*****

"""
def draw_triangle(t, num_rows):
    pass


"""
Exercise 3:

Very similar to the previous exercise, but the triangle is 
upside down, like so:

draw_triangle(t, 5) will produce output similar to the 
following:

*****
****
***
**
*

"""
def draw_upsidedown_triangle(t, num_rows):
    pass
        
"""
Exercise 4:

The draw_diamond function will take a turtle and total 
number of rows and draw a "diamond" shape, which is simply 
a normal triangle followed by an upside down triangle.

draw_diamond(t, 5) will produce output similar to the 
following:

*
**
***
**
*

draw_diamond(t, 6) will produce output similar to the 
following:

*
**
***
***
**
*

Noticed that depending if the number of rows is even or odd, we may 
nor may not repeat the middle row

"""
def draw_diamond(t, num_rows):
    pass
