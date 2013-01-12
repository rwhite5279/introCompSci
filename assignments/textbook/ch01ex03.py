# -------------- PROBLEM ----------------------

# Chapter 1, Programming Exercise #3
# Modify the Chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function. Your modified line of code should look like this:
#
#      x = 2.0 * x * (1-x)
#
# Run the program for various input values and compare the results to those obtained from the original program. Write a short paragraph describing any differences that you notice in the behavior of two versions.























































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get user input value ("seed")

#    Set up loop to run from ten times with the 3.9 multiplier (original)
#        change x
#        print new x
#    Set up loop to run from ten times with the 2.0 multiplier
#        change y
#        print new y
#    print paragraph describing difference in the two values

# Call the main function


























































# ch01ex03.py, modified for Ch1, Exercise#3
# From Zelle's Python Programming, Chapter 1
# By Richard White
# 2009-05-19

def main():
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    y = x              # Copy the input number into a second variable
    print ("Using 3.9 multiplier")
    for i in range(10): 
        x = 3.9 * x * (1-x)  
        print x
    print ("Using 2.0 multiplier")
    for j in range(10):   
        y = 2.0 * y * (1-y)    
        print y

    print 'Note that using a multiplier of 2.0 makes the "chaotic" function actually moved toward 0.5 as a final value.'

main()
