#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 8, Programming Exercise #5
# A positive whole number n>2 is prime if no number between 2 and square root(n) (inclusive) even divides n. Write a program that accepts a value of n as input and determines if the value is prime. If n is not prime, your program should quit as soon as it finds a value that evenly divides n.














































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get a positive whole number from the user (do some error checking on this!)
#    Is it 1 or 2? it's prime
#    If it's > 2, loop from 2 to square root (n)
#        if n divided by our current index number i divides evenly, print n and quit
#    If we get out of the loop without having found an n, the number must be prime. Tell user

# Call the main function
















































# -------------- PROGRAM -----------------------

# ch08ex05.py, Chapter 8, Exercise 5
# From Zelle's Python Programming, Chapter 7
# By Richard White
# 2009-08-03

# This program identifies whether or not a number entered by the user is prime.

def main():

	# Get a positive whole number (integer) from the user
	while True:
		positive_whole_number = input("Enter a positive whole number and I'll tell you if it's prime: ")
		
		# If the number isn't at least 1, or it doesn't equal its integer value, they messed up
		if ((positive_whole_number) < 1) or (int(positive_whole_number) != positive_whole_number):
			print "You didn't enter a positive whole number, silly!"
		else:
			break
	
	# Now loop through from 1 on up to start finding primes that sum to this number
	if (positive_whole_number == 1) or (positive_whole_number == 2):
		print positive_whole_number, "is prime! (That wasn't very difficult.)"
	else:
	
		# This is a little tricky. If we find a number that evenly divides, we can easily break out
		# of the loop, but at the end of the loop, we won't know if we broke out or if the loop just
		# ended. So we'll use a boolean FLAG--the variable "prime"--to keep track of how the loop
		# ended.
		prime = True  # Assume that we have a prime value
		for i in range (2, int(positive_whole_number ** 0.5 + 1)):   # Set up the loop
			if positive_whole_number % i == 0:						 # Check to see if the number
																	 # is evenly divisible
				print "Unfortunately,",positive_whole_number, "is evenly divisible by the value",i
				prime = False										 # Change status of flag
				break
		if prime:
			print "Yay!", positive_whole_number, "IS a prime number!"

if __name__ == "__main__":
    main()
    