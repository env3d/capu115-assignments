"""
    Practice with loops
    
    Here's the running version of the completed exercises: https://recordit.co/LuXlo3Vz6u 
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
    height = font_size / (1 - 0.39)
    turtle.setx(turtle.xcor() - (font_width / 2))
    turtle.sety(turtle.ycor() - (height / 2))
    turtle.write(letter, font=('Courier', font_size))
    turtle.setx(turtle.xcor() + (font_width / 2))
    turtle.sety(turtle.ycor() + (height / 2))

"""
Exercise 1 (do not use loop):
Modify the following function so the letter do not overlap
HINT:   move the turtle forward for a minimum amount after each draw_letter()
        Also, what is this best minimum amount?
"""

def exercise1():
    t = turtle.Turtle()
    t.penup()
    # The key observation here is that we need to pass our turtle
    # to draw_letter so the letter can be written to the screen
    #
    # Think of this as asking draw_letter to take over our turtle
    # for a short moment
    draw_letter(t, 'A')
    draw_letter(t, 'B')
    draw_letter(t, 'C')
    draw_letter(t, 'D')

"""
Modify the following so it uses a loop to print A, B, C, and D the 
same way as exercise 1
"""
def exercise2():
    t = turtle.Turtle()
    t.penup()
    for i in ['A', 'B', 'C', 'D']:
        draw_letter(t, 'A')
    
"""
Exercise 3:

This function takes a number as input, and draw numbers from 0 up to num, but not including num
i.e. exercise3(5) will draw 0 1 2 3 4 on screen

NOTE: assume that num will not exceed 10

"""
def exercise3(num):
    t = turtle.Turtle()
    t.penup()

"""
Exercise 4:

Draw 2 concentric semi-circles (no loop)
"""
def rainbow1():
    t = turtle.Turtle()

    radius = 50

    # Get the turtle into starting position
    t.pensize(5)
    t.left(90)

    # ready to draw
    t.pencolor('red')
    t.circle(-radius, 180)
    
    # go back to the beginning    
    t.right(90)
    t.forward(radius*2)
    
    # need to move to the starting position of the next semi-circle
    t.forward(5)
    t.right(90)

    # draw a slightly larger green semicircle 
    # also get rid of the bottom line
    
"""
Exercise 5:
Finally, use what you learned in exercise 4 and 
draw a rainbow with 7 colors

I have already started the loop for you
"""
def rainbow2():
    t = turtle.Turtle()
    radius = 50
    t.left(90)
    t.pensize(5)

    for c in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']:
        t.pencolor(c)
        t.forward(10)
    
    
