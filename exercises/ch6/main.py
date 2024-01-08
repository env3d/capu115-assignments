"""

The output of these exercises can be seen here: https://recordit.co/XWnpMDGXnn

"""

import turtle

"""
Exercise 1: Below is my incomplete solution to 
drawConcentricTriagles() from lab 4.  Complete it
by calling drawTriangle() inside the loop
of drawConcentricTriangles()


"""
def drawTriangle(side_length):
    t = turtle.Turtle()
    for i in range(3):
        t.forward(side_length)
        t.left(120)

def drawConcentricTriangles(num_triangles):
    for i in range(num_triangles):
        # call drawTriangle with appropriate input
        pass
        

"""
Exercise 2:

You will noticed from above, that the concentric triangles
are not expanding from the center.  One of the main
issue is that drawTriangle() creates a new turtle
everytime it is called.  

The concept used is covered here in the text, chapter 6.11

"""

def drawTriangle2(t, side_length):
    for i in range(3):
        t.forward(side_length)
        t.left(120)

def drawConcentricTriangles2(num_triangles):
    steve = turtle.Turtle()
    for i in range(num_triangles):
        # call drawTriangles2, and also reposition turtle
        pass

"""
Exercise 3:

Complete 6.13.2

"""

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawConcentricSquare():
    t = turtle.Turtle()
    pass        

"""
Exercise 4:

Draw the pattern shown in Exercise4Pattern.png under "Files"

Your solution will need to call 
drawSquareFromCenter() multiple times, based on the input
parameter
"""

def drawSquareFromCenter(t, sz):
    t.penup()
    t.forward(sz // 2)
    t.left(90)
    t.forward(sz // 2)
    t.right(180)
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.right(90)
    t.penup()
    t.forward(sz // 2)
    t.left(90)
    t.backward(sz // 2)
    t.pendown()
    

# This function takes as input the total number of squares to
# draw.  These squares must be spaced apart equally so you'll
# need to do some arithmetic based on turn angle
def drawPattern(num_squares):
    t = turtle.Turtle()
    pass


"""
Exercise 5:

Complete 6.13.10
"""
def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

def drawFiveStars():
    t = turtle.Turtle()
    pass
