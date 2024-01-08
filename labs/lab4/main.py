"""
  Lab 4: Draw some basic shapes with Turtle Graphics
         using loop algorithms.
 
  Author:  <your name>
  Date: <today>
"""
import turtle

"""
Exercise 1

Chatper 4.11 question 5 shows a few algorithms for drawing basic
shapes in turtle.  

Translate the triangle algorithm into the
function below, and make one important change - instead of
triangle of 100 units per side, the function below takes
a side_lenght as a parameter so you can draw a triangle
of any length from the console.  For instance:

# This will draw a triangle of 10 pixels per side
> drawTriangle(10) 
# This will draw a triangle of 100 pixels per side
> drawTriangle(100) 
"""

def drawTriangle(side_length):
    """ Draw an equilateral triangle using the given turtle, t """
    pass
  

"""
Exercise 2

Same as exercise 1, but draw a square instead.  The code is once
again given in 4.11 Q5

"""
def drawSquare(side_length):
    """ Draw a square using the given turtle, t """
    pass

"""
Exercise 3

Looking at all the solutions of 4.11 Q5, can you write a 
drawPolygon function that draws an arbitrary polygon
when given a number of sides and a side_length?

"""
def drawPolygon(num_sides, side_length):
    """ An arbitary polygon of equal sides """
    pass

"""
Exercise 4

This time, draw a rectangle of the specified lenght and width
Try to identfy where you can use a loop

"""
def drawRectangle(length, width):
    """ Draw a rectangle using the given turtle, t"""
    pass

"""
Exercise 5 (Challenge)

Create a drawing of multiple triangles nest inside one another.  Each 
time a triangle is nested, the size increase by 10

The basic algorithm is:

Loop num_triangles number of times:
    1. draw the smallest triangle of length 10 * the loop counter variable

HINT: from chatper 4.7, you are introduced to the range() function for
writing a loop.

The following code will print numbers 0 to 10 to the screen
for x in range(10):
    # sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(x)

instead of print, we will need to draw triangles instead
"""
def drawConcentricTriangle(num_triangles):
    pass

"""
This is an example that uses turtle to draw steps 10 px x 10 px
"""
def drawSteps(num_steps):
    t = turtle.Turtle()
    t.speed(0)
    for i in range(num_steps):
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
