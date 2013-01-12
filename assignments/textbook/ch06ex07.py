#!/usr/bin/python
# ---------------------------PROBLEM------------------------

# Chapter 6, Programming Exercise #7
# Write a function to compute the nth Fibonacci number. Use your function to solve Programming Exercise 16 from Chapter 3, which states:
# A Fibonacci sequence is a sequence of numbers where each successive number is the sum of the previous two. The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13,... [with the 0th number in the sequence being 0]. Write a program that computers the nth Fibonacci number, where n is a value input by the user. For example, if n = 6, then the result is 8.



































# --------------- PSEUDOCODE -------------------

# Get user's number that they want to find Fibonacci for (n)
# If it's 1, Fib = 1
# If it's > 1,
#     TwoNumsBefore = 0
#     OneNumBefore = 1
#     Start loop at i = 2, go till n        
#          Fib(i) = TwoNumsBefore + OneNumBefore
#          Print Fib (if you want to see what's happening
#          # Now realign the previous values
#          TwoNumsBefore = OneNumBefore
#          OneNumBefore = Fib
# print Fib



































































"""ch06ex07-whiter.py  
Fibonacci Function, by Richard White, 2011-03-07

This program calculates Fibonacci numbers using two different types of functions: one, a normal function that uses loops, and two, a recursive function (for recognition only)."""

import math, os, time

#############################################################
def fibonacci_classic(n):
    """This function gets the nth Fibonacci number using a loop."""
    if n != int(n):
        return "Error: n must be an integer"
    elif n < 1:
        return "Error: n must be 1 or greater"
    elif n == 1:
        fib = 1
    else:
        previous2 = 0
        previous1 = 1
        for i in range(2,n+1):
            fib = previous2 + previous1
            previous2 = previous1
            previous1 = fib
    return str(fib)             
	
###########################################################
def fibonacci_recursion(n):
    """This function gets the nth Fibonacci number using recursion."""
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        # print "We're recursing, getting Fibonacci #", n
        # print "by adding sum of Fibonacci #",n-1,"and Fibonacci #",n-2
        # wait = raw_input("[Enter] to continue...")
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


############################################################
def get_user_input():
    os.system("clear")  # Clears the screen
    print """This program calculates the nth number in the Fibonacci sequence,\nwhere each number in that sequence is the sum of the two previous numbers,\nand the 0th number is 0 and the 1st number is 1.\n\nThus, the sequence begins:\n1, 1, 2, 3, 5, 8, 13, 21, 34, 54, ...\n"""
    print "How would you like to calculate a Fibonacci number?"
    print "1) normally"
    print "2) recursively"
    print "3) exit program\n"
    return input("Your choice (1, 2, or 3)? ")
    
############################################################
def main():
    while True:
        choice = get_user_input()
        if choice == 3:
            break
        elif choice == 1:
            n = input("Which Fibonacci number would you like to calculate (positive integer >= 1)? ")
            print "The Fibonacci number is", fibonacci_classic(n)
        elif choice == 2:
            print "WARNING! Calculating Fibonacci numbers greater than 30 or so\ncan cause significant lag on your machine."
            n = input("Which Fibonacci number would you like to calculate (positive integer >= 1)? ")
            print "The Fibonacci number is:", fibonacci_recursion(n)
        else:
            print "I'm sorry, please choose 1, 2, or 3"
        time.sleep(3)    
        
    print "Thanks for calculating Fibonaccis with us!"

#############################################################
if __name__ == "__main__":
    main()
	
	