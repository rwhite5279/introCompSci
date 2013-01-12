#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 7, Programming Exercise #3
# A certain CS professor gives 100-point quizzes that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts an exam score as input and uses a decisions structure to calculate the corresponding grade.










































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the exam score
#    If exam_score >=90 then it's an A
#        else if it's >=80 then it's a B
#        else if it's >=70 then it's a C
#        else if it's >=60 then it's a D
#        else it's an F
#    Print out grade

# Call the main function






































# -------------- PROGRAM -----------------------

# ch07ex03.py, Chapter 7, Exercise 3
# From Zelle's Python Programming, Chapter 7
# By Richard White
# 2009-08-03

# This program converts exam scores to letter grades

def main():

	# Get the exam score and error check to make sure it falls within the required range
    while True:
    	exam_score = input("Please enter the exam score, 0-100: ")
    	if 0 <= exam_score <=100: 
    		break    # Exit this error checking loop if the number is valid
    	else:  
    		print "Sorry: you entered an invalid exam score of",exam_score
    
    # Compare the entered exam score with the specified cut-off values to determine the
    # appropriate letter grade
    if exam_score >= 90:
    	letter_grade = "A"
    elif exam_score >= 80:
    	letter_grade = "B"   
    elif exam_score >= 70:
    	letter_grade = "C"
    elif exam_score >= 60:
    	letter_grade = "D"    
    else:
    	letter_grade = "F"
    print "The equivalent letter grade is: ",letter_grade

if __name__ == "__main__":
    main()
