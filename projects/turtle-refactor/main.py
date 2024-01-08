import turtle

"""
In this project you will create a beautiful symmetric drawing (sometimes called mandala)

you will notice that there is a lot of code repetition. Your task is to rewrite the 
code so it still draws the same picture, but it uses only two functions. Each of the 
functions you write has to be very short (about 4 lines of code). In order to 
accomplish that, you need to add additional parameters to each function.

To start, figure out what the current function parameters do. Then figure out how the 
functions are different and how you can introduce new parameters to have only one 
function that replaces all the ones with the same name.

In the final program you submit you should be able to change only one line of code in 
order to produce a drawing that contains a different number of petals.
"""

"""
Exercise 1:

Notice that all drawCircles functions are practically the same, except for the number 
of circles drawn and the resizing in each for loop iteration. 

Write a function called drawCircles to replaces all of the functions. 
drawCircles should have two additional parameters to accommodate these varying 
values. 
"""

def drawCircles4(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4

def drawCircles5(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5

def drawCircles10(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10

def drawCircles19(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19

def drawCircles20(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20


"""
Exercise 2:

Similar to Exercise 1, replace all instances of drawSpecial function with one 
function that uses  parameters. Your function must call the drawCircle function 
you developed in exercise 1.

Each of the functions you write in Step 2 and Step 3 should be very short (about 4 
lines of code). 

"""

def drawSpecial4(t,size,repeat):
  for i in range (repeat):
    drawCircles4(t,size)
    t.right(360/repeat)

def drawSpecial5(t,size,repeat):
    for i in range (repeat):
        drawCircles5(t,size)
        t.right(360/repeat)

def drawSpecial10(t,size,repeat):
    for i in range (repeat):
        drawCircles10(t,size)
        t.right(360/repeat)
        
def drawSpecial19(t,size,repeat):
    for i in range (repeat):
        drawCircles19(t,size)
        t.right(360/repeat)        
        
def drawSpecial20(t,size,repeat):
    for i in range (repeat):
        drawCircles20(t,size)
        t.right(360/repeat)


"""
Exercise 3:

At this point, you would have created 2 new functions: drawCircles and drawSpecial.

Your job is now to rewrite draw_picture() so that it uses the 2 new functions 
from Exercises 1 and 2.

The rewritten version of draw_picture() will also meet the following constraints:

  - Use 1 turtle instead of multiple turtles
  
  - Use a loop with a list of colors to change the turtle color, similar to
    the following code snippet.  
    
    HINT: You will need to write a compound if statement
    inside the body of the loop to control how each color is drawn. 

        ...
        colours = ['white', 'yellow', 'blue', 'orange', 'pink']
        for c in colours:
            t.color(c)
            ...


"""
def draw_picture():

    wn = turtle.Screen()
    wn.bgcolor('black')
    Albert = turtle.Turtle()
    Albert.speed(0)
    Albert.color('white')
    drawSpecial4(Albert,100,10)
    
    Steve = turtle.Turtle()
    Steve.speed(0)
    Steve.color('yellow')
    drawSpecial10(Steve,100,10)
    
    Barry = turtle.Turtle()
    Barry.speed(0)
    Barry.color('blue')
    drawSpecial5(Barry,100,10)
    
    Terry = turtle.Turtle()
    Terry.speed(0)
    Terry.color('orange')
    drawSpecial19(Terry,100,10)
    
    Will = turtle.Turtle()
    Will.speed(0)
    Will.color('pink')
    drawSpecial20(Will,100,10)
