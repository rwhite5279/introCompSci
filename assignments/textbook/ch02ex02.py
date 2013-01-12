# -------------- PROBLEM ----------------------

# Chapter 2, Programming Exercise #2
# Modify the avg2.py program (Section 2.5.3) to find the average of three exam scores.
#
# The original program looked like this:
#
# avg2.py
# A simple program to average two exam scores
# Illustrate use of multiple input

# def main():
#     print "This program computes the average of two exam scores."
#    
#     score1, score2 = input("Enter two scores separated by a comma: ")
#     average = (score1 + score2) / 2.0
#
#     print "The average of the sores is:", average
#
# main()

















































# -------------- PSEUDO CODE -------------------

# Define the main function
#     get the three numbers to be average
#     calculate the average and print it
#
# Call the main function




























































# ch02ex02.py
# From Zelle's Python Programming, Chapter 2
# By Richard White
# 2011-02-02

def main():
    a, b, c = input("Enter three numbers, separated by commas: ")
    avg = (a + b + c) / 3.0   # Use 3.0 to get a real (decimal) result
    print "The average of your three numbers is ",avg
    
main()





"""NOTE FROM THE PROGRAMMER
Obviously this technique becomes a bit cumbersome if you have more numbers that need to be averaged. How about a for-loop to really do this right? There are a couple of tricks here that you haven't really learned about, but you get the idea...

from __future__ import division

def main():
    n = input("How many numbers do you want to average? ")
    total = 0
    for i in range(1,n+1):
        print "Enter #",i,
        the_number = input()
        total = total + the_number
    average = total / n
    print "The average of the",n,"numbers that you entered is",average

main()
  
"""




