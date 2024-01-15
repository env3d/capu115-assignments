"""
The following is a very basic introduction on the concepts of OOP.  It's not
meant to be comprehensive.  Rather, it tries to demystify some of the syntax we
use in this class.

You have seen how to create a turtle:

    t = turtle.Turtle()

We can then have draw pictures using the turtle:

    t.penup()
    t.forward(50)

You have also seen how to create a pixel and an image

    p = image.Pixel(255,255,255)
    print("this pixel has the color", p.getRed(), p.getGreen(), p.getBlue())
    
    im = image.EmptyImage()
    im.setPixel(5, 60, p)

Even how to split a string:

    s = "this is a string"
    tokens = s.split()

In all the above instances, we first create an OBJECT, we then call functions on the OBJECT to 
have it perform certain computations.  The one thing to note is that computation is 
perform on the OBJECT.  Or rather, when the function is called, the OBJECT state is changed
in some ways.  

Read the object description from chapter 17.3 to 17.6 from the textbook.

We are now going to explore the syntax to create your own objects.
"""

"""
Exercise 1

Imagine we are creating an class called point, which represents
a point on a 2D plane.  

Complete the following code such that getDistanceFromOrigin() would perform as expected:

> p1 = Point(3,4)
> p2 = Point(0,3)
> p3 = Point(4,0)
> p1.getDistanceFromOrigin()
5
> p2.getDistanceFromOrigin()
3
> p3.getDistanceFromOrigin()
4

"""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDistanceFromOrigin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

"""
Exercise 2

Below is a UTC_Time class.  To create an object of the time class, you will need
to provide an hour and a minute.

You can use the UTC_time class as follows:

> t = UTC_Time(12, 30)
> t.format()
'12:30'

Write a method format_PDT and returns a string that represents the time in 
pacific daylight savings time. 

NOTE: PDT is UTC - 7 hours.  So if the time is 12:30 UTC, it is 5:30 in PDT
"""

class UTC_Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def format(self):
        return str(self.hour) + ":" + str(self.minute)
    
    def format_PDT(self):        
        if self.hour < 7:
            pass
        else:
            return str(self.hour - 7) + ":" + str(self.minute)

"""
Exercise 3

Classes is great for code organization where you can group data based
on larger entities.  For instances, imagine you want to create a 
way to calculate student grades.  Previously, we would write a function
like this:

def calculate_grade(a1, a2, exam):
    return (a1/20) * 0.1 + a2/40 * 0.3 + exam/100 * 0.6

The above function describes a class containing 2 assignemnts and one exam.
a1 is out of 20 and worth 10% of the final grade
a2 is out of 40 and worth 30% of the final grade
exam is out of 100 and worth 60% of the final grade

If you need calculate grades for multiple students, you may write the 
following code:

josh = calculate_grade(10, 30, 100)
amy = calculate_grade(20, 35, 90)
if josh > amy:
    print('Josh has a higher overall grade')
else:
    print('Amy has a higher overall grade')

The issue with the above code however, is that nowhere in my above code
do we create a relationship between josh and each individual grade items, 
josh is simply a float.

If we rewrite our grade calculation using classes, we can have the following
code:

josh = Grade(10, 30, 100)
amy = Grade(20, 35, 90)
if josh.get_final() > amy.get_final():
   print('Josh has a higher overall grade')
else:
    print('Amy has a higher overall grade')

But it will also allow us to write code like this:

josh = Grade(10, 30, 100)
amy = Grade(20, 35, 90)
if josh.get_exam() > amy.get_exam() and josh.get_final() < amy.get_final():
   print('Josh has a higher exam grade but lower final grade')

Complete the following class definition so the above code 
can execute properly:
"""

class Grade:
    def __init__(self, a1, a2, exam):
        self.a1 = a1
        self.a2 = a2
        self.exam = exam

    def get_a1(self):
        return self.a1

    def get_a2(self):
        return self.a2

    def get_exam(self):
        return self.exam

    def get_final(self):
        return (self.a1/20) * 0.1 + self.a2/40 * 0.3 + self.exam/100 * 0.6
