#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 4, Programming Exercise #7
# Expand your solution to the previous problem (calculating the numeric value of a series of character) to allow the calculation of a complete name such as "John Marvin Zelle" or John Jacob Jingleheimer Smith." The total value is just the sum of the numeric values of all the names.




























# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the input from the user, a string
#    Remove any blank spaces from the string
#    Go through each character in the string
#        convert the character to an appropriate number
#        add that number to a running total
#    Print out the running total

# Call the main function






















# -------------- PROGRAM -----------------------

# ch04ex07.py, Chapter 4, Exercise 7
# From Zelle's Python Programming, Chapter 4
# By Richard White
# 2009-07-04

# This program prints out the "numeric value" of a name

def main():

    import string   # needs this module for various string processing functions
    
    string_with_spaces = raw_input("Please enter a name: ")
    
    # There are different ways of "getting rid of the spaces" in a string.
    # Here, we'll just split the names up into words and then go through
    # word. This is an example of a nested loop
    
    string_with_spaces = string.lower(string_with_spaces) # Convert names
                                                          # to lower case
    name_list = string.split(string_with_spaces," ")      # Split names up
    num_value = 0                                         # Initialize counter
    for name in name_list:                                # For each name...
        for letter in name:                               # For each letter...
            num_value = num_value + (ord(letter)-96)      # a = 97, so a = 1

    print "Your numerical value is", num_value            # Print out total

main ()
