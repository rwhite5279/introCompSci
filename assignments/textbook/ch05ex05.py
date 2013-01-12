#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 5, Programming Exercise #5
# Numerologists claim to be able to determine a person's character traits bsed on the "numeric value" of a name. The value of a name is determined by summing up the values of the ltters of the name where "a" is 1, "b" is 2, "c" is 3, etc, up to "z" being 26. For example, the name "Zelle" would have the value 26+5+12+12+5 = 60 (which happens to be a very auspicious number, by the way). Write a program that calculates the numeric value of a single name provided as input.


























# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the input from the user, their name
#    for each character in their name:
#        convert it to a number, and add it to the total
#    display the total

# Call the main function






















# -------------- PROGRAM -----------------------

# ch05ex05.py, Chapter 5, Exercise 5
# From Zelle's Python Programming, Chapter 5
# By Richard White
# 2011-02-11

# This program converts a string to a "numerology" number

def main():
    
    userName = raw_input("Please enter your name, and I'll convert it to a number: ")
    userNumber = 0  # initialize
    for character in userName:
        # convert to lower case...
        # convert to ordinal form
        # subtract so that a = 1
        # add to total
        if character != " ":
            userNumber = userNumber + ord(character.lower())-96
    print userNumber

main ()










