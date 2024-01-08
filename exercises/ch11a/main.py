"""
These exercises are based on section 11.4, with a text file named ccdata.txt
"""

"""
return the total amount of emissions for the entire dataset

> calculate_total_emission()
189.510001278
"""
def calculate_total_emission():

    total_emission = 0
    
    ccfile = open("ccdata.txt", "r")        
    for aline in ccfile:
        values = aline.split()
        # This is where you use the accumulator pattern to sum up all the emissions
        total_emission = 0
        
    ccfile.close()

    return total_emission


"""
Sometimes we want to search over our dataset and only include
certain lines in our calculation.  In this exercise, 
the function takes in 2 argument, start_year and end_year.

Complete the function such that we calculate the total emissions
for year >= start_year and year <= end_year

i.e.

> calculate_emission_range(1900,1920)
9.73
> calculate_emission_range(2000,2020)
90.9

"""
def calculate_emission_range(start_year, end_year):    
    total_emission = 0
    ccfile = open("ccdata.txt", "r")        
    
    # use the accumulator pattern here, but this time you also need 
    # an IF statement
            
    ccfile.close()
    return total_emission


"""
return the average tempreture for the entire dataset

> calculate_avg_temp()
-0.055
"""
def calculate_avg_temp():

    # see if you can come up with all the necessary code
    return -1
 


"""
return the average tempreture for year >= start_year and year <= end_year

> calculate_avg_temp_range(1900, 1920)
-0.3133333333333333
> calculate_avg_temp_range(2000, 2020)
0.53
 
"""
def calculate_avg_temp_range(start_year, end_year):

    return -1
 


"""
The following function is directly from text.  Modify it to write the reformatted data to 
a file called annotated_data.txt.  As per 11.6
"""
def reformat_data():
    ccfile = open("ccdata.txt", "r")
    outfile = open("annotated_data.txt", "w")
    for aline in ccfile:
        values = aline.split()
        # modify the following line to write to a file instead of printing to console
        print('In ' + values[0] +' the average temp. was ' + values[1] + ' °C and CO2 emmisions were ' + values[2] +  ' gigatons.')
    
    ccfile.close()


