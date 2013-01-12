# -------------- PROBLEM ----------------------

# Chapter 3, Programming Exercise #15
# Write a program that approximates the value of pi by summing the terms of this series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... The program should prompt the user for n, the number of terms to sum, and then output the sum of the first n terms of this series. Have your program subtract the approximation from the value of math.pi to see how accurate it is.















































# -------------- PSEUDO CODE -------------------

# Import the math library
# Define the main function

#    Ask how many terms the user wants to sum

#    Set initial variables for the pi_calculation

#    Set up a loop that will get to the appropriate term number
#        Subtract this term, and add the next term to pi_calculation

# When done with the loop print out the pi_calculation and the "real" pi

# Call the main function





































# -------------- PROGRAM -----------------------

# ch03ex15.py, Chapter 3, Exercise 15
# From Zelle's Python Programming, Chapter 3
# By Richard White
# 2009-06-02

# This program compares an internal calculation of pi to the "real" thing,
# as contained in the math library

import math # This route makes use of the math library
from __future__ import division


def main():
    print "This program is going to calculate pi and compare it to"
    print "the value of pi contained in the Python 'math' library."
    print
    n = input ("How many terms do you want to sum?")
    pi_calc=0         # Initializing our pi counter
    print "Summing ",n," terms..."
    for i in range(1,n*4,4):
        # print i
        pi_calc = pi_calc + 4/i - 4/(i+2)
    print "%0.20f" % (pi_calc) 
    print "%0.20f" % (math.pi)  
    print
    percent_diff = abs(((pi_calc-math.pi)/(math.pi))*100)   
    print "The two values are off by ", percent_diff, "%"    


main()


