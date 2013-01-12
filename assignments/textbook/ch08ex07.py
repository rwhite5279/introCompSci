#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 8, Programming Exercise #7
# The Goldbach conjecture asserts that every even number is the sum of two prime numbers. Write a program that gets a number from the user, checks to make sure that it is even, and then finds two prime numbers that sum to the number.





















































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get a number from the user
#    Check to make sure that it's an even number
#    Loop through numbers less than the number to find out
#        a. Do we have a prime number? (Use solution from #5, perhaps set up as a function?)
#        b. If so, what's the other number that would add to make our even number?
#        c. Is this second number a prime number? If so, we're done!

# Call the main function












































# -------------- PROGRAM -----------------------

# ch08ex07.py, Chapter 8, Exercise 7
# From Zelle's Python Programming, Chapter 7
# By Richard White
# 2009-08-03

# This program attempts to apply the Goldbach conjecture to a numeric value entered by the user

# The function "is_prime" determines whether the parameter n is prime or not
def prime(n):
	if (n < 1) or (int(n) != n):
		is_prime = False
	elif (n == 1) or (n == 2):
		is_prime = True
	else:
		is_prime = True
		for i in range (2, int(n ** 0.5 + 1)):
			if n % i == 0:
				is_prime = False
				break
	return is_prime

# This is the main function that gets user input, then examines it using the prime function
def main():
	while True:
		even_number = input("Enter an even number, and we'll find two primes whose sum is that number: ")
		if (even_number % 2) == 0:
			break	# If there's no remainder from dividing by 2, we have an even number
		else:
			print even_number, "is not an even number, silly!"
	
	# Now loop through from 1 on up to start finding primes that sum to this number
	for n in range(1, even_number):	
		if prime(n):
			if prime(even_number - n):
				print "Two primes that add up to make",even_number,"are",n,"and",even_number - n
				break

if __name__ == "__main__":
    main()


