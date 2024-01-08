"""
Question: Imagine if you cannot use loops (no for, no while).  How do you create a loop?

Answer: We use a technique called recursion... i.e. function that calls itself

Reference: Textbook chapter 16.1 - 16.3
"""

"""
Examples
"""
def add_loop(n):
    """
    Here, we have a basic function that uses the accumulator pattern to add
    numbers from 0 to n, where n is the input assuming n > 0
    """
    acc = 0
    for i in n:
        acc = acc + i
    return acc

def add_recursion(n):
    """
    This is the recursive version of the same function.  The key line is 
    the return line, where we add n with the result from calling itself.

    The best way to look at recursion is to try to write out the 
    return line give an certain input.  
    i.e.
    add_recursion(1) == 1 + add_recursion(0) == 1 + 0
    add_recursion(2) == 2 + add_recursion(1) == 2 + 1 + add_recursion(0) == 2 + 1 + 0
    """
    if n == 0:
        return 0
        
    return n + add_recursion(n-1)

def mult_list(lst):
    """
    A basic example of list processing with recursion.  
    This function returns a new list where each item is multiplied by 2

    For list processing functions, we reduce the number of list items 
    by 1 every time until it reaches an empty list
    """
    if lst == []:
        return []

    return [ lst[0] * 2 ] + mult_list(lst[1:])

"""
Exercise 1 (from text 16.8.1)

Write a recursive function to compute the factorial of a number.
(this is very similar to add_recursion from above)

factorial(3) == 3 * 2 * 1
"""

def factorial(n):
    return 0
    
"""
Exercise 2

Modified the mult_lst so that we return the square of each list item 
"""

def square_lst(lst):
    return []

"""
Exercise 3 (from text 16.8.2)

Write a recursive function to reverse a list.
"""

def reverse(lst):
    return []

"""
Exercise 4

Write a recursive function that counts the number of the character w that appears in a string:

> count3('what who how')
3
> count3('nothing')
0
"""

def countw(sentence):
    return 0

"""
Exercise 5 

Write a recursive function to check for palindrome
"""
def palindrome(word):
    return True
