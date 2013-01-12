# -------------- PROBLEM ----------------------

# Chapter 2, Programming Exercise #4
# Modify the convert.py program (Section 2.2) so that it computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C.























































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Set up loop to run from 0 to 100, by 10s (0, 10, 20,... 100)
#        Calculate Fahrenheit temperature
#        Print Celsius and Fahrenheit temperatures

# Call the main function

















































# convert.py, Chapter 2, Exercise 4
# From Zelle's Python Programming, Chapter 2
# By Richard White
# 2009-05-19

# This modified version of the temperature conversion program computes and prints a table of equivalent Celsius and Fahrenheit temps every 10 degrees, from 0C to 100C.

def main():
    for i in range (11): 
        celsius = i * 10  
        # the previous lines set up a loop for 0, 10, 20,.. 100
        # Can also use this for the loop:
        #     for i in (0,10,20,30,40,50,60,70,80,90,100):
        fahrenheit = (9.0 / 5.0) * celsius + 32   
        print "%6.2f degrees C = %6.2f degrees F" % (celsius, fahrenheit)    
        # Note that the line above includes 'string formatting', which 
        # makes the table look a lot neater. We haven't learned about that
        # yet, so your program doesn't need to have that formatting!
main()

