#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 8, Programming Exercise #1
# The Fibonacci sequence starts 1, 1, 2, 3, 5, 8,... Each number in the sequence (after the first 2) is the sum of the previous two. Write a program that computes and outpts the nth Fibonacci number, where n is a value entered by the user.














































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Ask user which Fibonacci number they want (> 2)
#    Start Fibonacci counter at 2
#    n1 = 1, n2 = 1
#    Add together to get next number

# Call the main function
















































# -------------- PROGRAM -----------------------

# ch08ex01.py, Chapter 8, Exercise 1
# From Zelle's Python Programming, Chapter 8
# By Richard White
# 2011-01-20

# This program calculates the nth Fibonacci number

def main():

	# Get a positive whole number (integer) from the user
	while True:
		n = input("Enter a positive integer and I'll give you the value at that place in the Fibonacci sequence: ")
		
		# If the number isn't at least 1, or it doesn't equal its integer value, they messed up
		if ((n < 1) or int(n != n)):
			print "You didn't enter a positive whole number, silly!"
		else:
			break
	
	    # Now loop through from 1 on up to start finding primes that sum to this number
        print "Fibonacci number 1 is 1"
        fib_num = 1
        prev1 = 0
        prev2 = 1
        while (fib_num < n):
            fib_num += 1
            fib = prev1 + prev2   # get next fibonacci number
            prev1 = prev2   # replace old value
            prev2 = fib     # replace old value
            print "Fibonacci number",fib_num,"is",fib

	        


if __name__ == "__main__":
    main()
    