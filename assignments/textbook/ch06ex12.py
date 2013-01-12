#!/usr/bin/python
# ---------------------------PROBLEM------------------------

# Chapter 6, Programming Exercise #12
# Write and tst a function to meet this specification.
# sumList(nums)     nums is a list of numbers. Returns the sum of the numbers in the list.



































# --------------- PSEUDOCODE -------------------

# Get user's list of numbers
# for each number in the list
#     Add it to a total
#     return the total




































































"""ch06ex12-whiter.py  
Fibonacci Function, by Richard White, 2011-03-07

This program calculates a sum of numbers in a list."""

############################################################
def get_numbers():
    print "Enter some numbers. Hit the [Enter] key when done, and I'll find the sum."
    myList = []
    next = "nothing"
    while True:
        aNumber = raw_input("Enter a number: ")
        if aNumber == "": break
        myList.append(aNumber)
    return myList
    
############################################################
def sum_numbers(nums):
    total = 0
    for aNum in nums:
        total = total + float(aNum)
    return total


############################################################

def main():
    nums = get_numbers()
    print "The total is",sum_numbers(nums)

    

#############################################################
if __name__ == "__main__":
	main()
	
	