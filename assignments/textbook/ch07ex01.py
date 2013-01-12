#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 7, Programming Exercise #1
# Many companies pay time-and-a-half for an hours worked above 40 in a given week. Write a program to input the number of hours worked and the hourly rate and calculate the total wages for the week.










































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Ask for how many hours worked this week and how much the hourly pay rate is
#    If the number of hours worked is 40 or less:
#        Calculate pay = hours * pay_rate
#    else 
#        Calculate pay = (40 * pay_rate) + ((hours - 40) * 1.5 * (pay_rate))

# Call the main function







































# -------------- PROGRAM -----------------------

# ch07ex01.py, Chapter 7, Exercise 1
# From Zelle's Python Programming, Chapter 7
# By Richard White
# 2009-08-03

# This program calculates pay, along with overtime pay, if over 40 hours per week are worked

def main():

    hours, pay_rate = input("Please enter the hours worked this week, and your base pay rate: ")
    if hours <= 40: 
        pay = hours * pay_rate  
    else:
        pay = (40* pay_rate) + ((hours - 40) * (pay_rate * 1.5))   
    print "This week, you'll be paid $%0.2f" % (pay)    

if __name__ == "__main__":
    main()
