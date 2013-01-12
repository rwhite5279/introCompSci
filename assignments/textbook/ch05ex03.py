# -------------- PROBLEM ----------------------

# Chapter 4, Programming Exercise #4
# A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89: B, 70-79: C, 60-69: D, <60: F. Write a program that accepts an exam score as input and prints out the corresponding grade.














































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the input from the user, a number 0-100
#    Check (a list?) to see what the corresponding letter grade is
#    Print out the letter grade

# Call the main function








































# -------------- PROGRAM -----------------------

# ch04ex04.py, Chapter 4, Exercise 4
# From Zelle's Python Programming, Chapter 4
# By Richard White
# 2009-07-02

# This program has the user enter a number grade on a 0-100 scale and then
# prints out a corresponding letter grade.

def main():

    # Set up list of grade values to match points entered by user
    grades = ["F","F","F","F","F","F","D","C","B","A","A"]

    # How to get appropriate index from 0-100?
    # This is a little clunky. Probably makes more sense to use an if-else
    # statement when we learn about those.
    
    score = input("Please enter the points earned on the assignment (0-100): ")
    index = score/10
    print "The student earned a",grades[index],"on that assignment."

main ()
