#!/usr/bin/python
"""Selection Sort, by Richard White
   2010-01-19
   This program demonstrates the classic selection sort algorithm by filling up a list of 1000 numbers with random numbers, and then sorting them.

   The selection sort algorithm works like this:
   1. Go through the list and find the smallest value
   2. Place that value first in the list
   3. Repeat, starting at 2nd position: go through list, \
        find smallest item on list, and place it in 2nd position.
   4. Go through entire list until done.
"""










































"""
PSEUDOCODE FOR SELECT SORT PROGRAM
# Fill up list with 1000 random numbers

# Do Selection Sort on list

# Print out the sorted list
"""



















































"""
MORE DETAILED PSEUDOCODE

# import random module

# Fill up list with 1000 random numbers:
# create empty list of numbers called... listOfNumbers?
# for i in range(1000):
#    append a random integer to the listOfNumbers

# Do the Selection Sort
# for i in range(0,1000):
#     for j in range(i+1,1000):
#         if listOfNumber[i] > listOfNumbers[j]:
#              swap those two numbers

# Print out the sorted list
# for aNumber in listOfNumbers:
#     print aNumber

"""









































"""Selection Sort, by Richard White
   2010-01-19
   This program demonstrates the classic selection sort algorithm by filling up a list of 1000 numbers with random numbers, and then sorting them.

   The selection sort algorithm works like this:
   1. Go through the list and find the smallest value
   2. Place that value first in the list
   3. Repeat, starting at 2nd position: go through list, find smallest item on list, and place it in 2nd position.
   4. Go through entire list until done.
"""

import random

def main():
    listOfNumbers = []
    for i in range(1000):
        listOfNumbers.append(random.randrange(1000))

    print listOfNumbers

    for i in range(0,len(listOfNumbers),1):     # Begin looking through list from first item
        for j in range(i+1,len(listOfNumbers),1):  # Go through starting with next item
            if listOfNumbers[j] < listOfNumbers[i]:
                listOfNumbers[j],listOfNumbers[i] = listOfNumbers[i],listOfNumbers[j]
    print listOfNumbers

if __name__ == "__main__":
    main()
   
