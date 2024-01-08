"""

This is a starter project for the energy expenditure exercise.
I have created some of the function definitions for you to get 
you going.

Details of this project can be found at 

https://docs.google.com/document/d/1eME5AMNNMwkvRzPWuw8GyE_kx1jkKGJfDcW0enAMFXQ/edit?usp=sharing

Here is a complete running version: https://recordit.co/Z276xmNSsc 

"""

def pounds_to_kilos(pounds):
    """
    Given pounds as input, return the corresponding kilos using the 2.2 as conversion factor
    """
    return 0

def inches_to_centimeters(inches):
    """
    Given inches as input, return the corresponding centimeter using the 2.54 as conversion factor
    """
    return 0

def calculate_bmr(weight, height, gender, age):
    """
    This function takes in 4 inputs:

    weight in kilos
    height in centimeters
    gender is a string of 1 character, either 'M' or 'F'
    age is an integer
    
    HINT: you will need to use different formulas for different gender
    perfect opportunity to use a simple if statement
    here's a quick overview of if: https://www.w3schools.com/python/python_conditions.asp 
    """
    return 0

def calculate_activity_expenditure(bmr, activity_factor):
    """
    There are 2 inputs to this function, the bmr and activity_factor
    The activity factor is based on the following table:
    
    Sedentary - mostly resting with little or no activity  : 0.25
    Light - occasional unplanned activity e.g. going for a walk, or a swim or skiing: 0.375
    Moderate - daily planned activity such as short jogs, brisk walk: 0.55
    Heavy - daily planned workouts (hours or several hours of continuous activity: 0.775
    
    For example, if the bmr is 1600 and the person has a sedentary lifestyle, then we would 
    call the function from the console follows:
    
    > calculate_activity_expenditure(1600, 0.25)
    400.0
    """
    
    return 0

def calculate_food_expenditure(daily_calories):
    """
    Food expenditure is calculated as 5% of the daily caloric intake
    """
    return 0

def test():
    """
    You will need to write some assert statements to make make 
    sure that each function is working properly
    I have create 1 assert for you, you will need to have at least 2
    asserts per function

    For a discussion on asserts, see 
    https://runestone.academy/ns/books/published/learn_to_code/Functions/UnitTesting.html
    """
    assert(pounds_to_kilos(2.2) == 1.0)


def main():
    """
    The "main" program, i.e. user interface 
    this is also known as the entry point of your program.  
    Conceptually, The user interface is the only place where you should use 
    input and print.

    For a discussion on main function, see
    https://runestone.academy/ns/books/published/learn_to_code/Functions/mainfunction.html 

    NOTE: you can skip the "Advanced Topic"
    """
    
    # I have filled in the first 2 input statement, you will need to do the rest
    weight = input('Your weight in pounds: ')
    height = input('Your height in inches: ')
    gender = 'M'
    age = 25
    calorie_intake = 3000

    # Before asking the user for their activity level, it may be a good idea to display
    # the activity table so users would know what to enter.
    activity_level = 0.55

    # The total daily expenditure is the sum of bmr, activity expenditure, and food expenditure
    total_daily_expenditure = 0

    print('Your total daily expenditure is ' + total_daily_expenditure)
