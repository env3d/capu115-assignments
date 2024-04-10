#
# Loops can be thought of as patterns 
# Below are a few basic loop patterns we have covered in class

# This first pattern simple repeats using the range() function
def for_loop_with_range(num):
    count = 0
    for i in range(num):
        count = count + 1
    return count

# We can add IF statements inside the loop 
def for_loop_with_selection(num):
    count = 0
    for i in range(num):
        if i % 2 == 0:
            count = count + 1
    return count

# Using for loop to process a list of items (or characters inside a string)
def for_loop_with_list(lst):
    count = 0
    for item in lst:
        if len(item) > 5:
            count = count + 1
    return count

# Using for loop to find an item in a list
def for_loop_search(lst, target):
    found = False
    for item in lst:
        if item == target:
            found = True
    return found

# Using for loop to find an item in a list (short-circut using break)
def for_loop_search_with_break(lst, target):
    found = False
    for i in lst:
        if i == target:
            found = True
            break
    return found

# Using for loop to find an item in a list (short-circut using return)
def for_loop_search_with_return(lst, target):    
    for i in lst:
        if i == target:
            return True            
    return False

# This is a pattern to create a new list
def for_loop_produce_new_list(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i**2)
    return new_lst

# Note that all for loops can be re-written using while loops
def while_loop_produce_new_list(lst):
    new_lst = []

    i = 0
    while i < len(lst):
        new_lst.append(i**2)
        i = i + 1
        
    return new_lst
