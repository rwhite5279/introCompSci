# -------------- PROBLEM ----------------------

# Chapter 4, Programming Exercise #3
# A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an input and prints out the corresponding grade.













































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the input from the user, a number 0-5
#    Check (a list?) to see what the corresponding letter grade is
#    Print out the letter grade

# Call the main function












































# -------------- PROGRAM -----------------------

# ch04ex03.py, Chapter 4, Exercise 3
# From Zelle's Python Programming, Chapter 4
# By Richard White
# 2009-07-02

# This program has the user enter a number grade on a 0-5 scale and then
# prints out a corresponding letter grade.

def main():

    # Set up list of grade values to match points entered by user
    grades = ["F","F","D","C","B","A"]

    score = input("Please enter the points earned on the assignment (0-5): ")

    # Extra credit for using the correct article--"a" or "an"--depending on
    # the letter of the grade that's assigned. We haven't learned yet how
    # to do if-else statements, but here's an introduction to them.

    if (score > 1) and (score < 5):
        article = "a"
    else:
        article = "an"

    print "The student earned",article,grades[score],"on that assignment."

main ()
