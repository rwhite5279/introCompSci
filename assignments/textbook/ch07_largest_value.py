#!/usr/bin/python

# A simple maximum value decision-making program

def main():
	x1, x2, x3 = input("Please enter three numeric values: ")
	maxnum = x1
	if x2 > maxnum:
		maxnum = x2
	if x3 > max:
		maxnum = x3
	print "The maximum value you entered was",maxnum
	print "The maximum value you entered, according to the max function, was", max(x1,x2,x3)

# Run this program automatically if it hasn't been imported
if __name__ == '__main__':
	main()
	