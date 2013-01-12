#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 11, Programming Exercise #11
# Write an automated censor program that reads in the text from a file and creates a new file where all of the four-letter words have been replaced by "****". You can ignore punctuation, and you may assume that no words in the file are split across multiple lines. (Note from Mr. White: This exercise is being modified so that the program accepts input from the user, not from a file.)






















































# -------------- PSEUDO CODE -------------------

# Define the function censor()

#    while the user enters lines:
#        Get a line of input from the user
#        Look for a curse word, if found
#        Replace the curse word with ****
#        Print out the new line.

# Call the function censor()
















































# -------------- PROGRAM -----------------------

# ch11ex11.py, Chapter 11, Exercise 11
# From Zelle's Python Programming, Chapter 11
# By Richard White
# 2011-02-15

# This program takes censors lines of input entered by the user

def main():
   	userText = raw_input("Enter text ("" to quit): ")
   	while userText != "":
   	    for cussword in ("shit","damn","fuck","poop"):
   	        userText = userText.lower().replace(cussword,"****")
   	    print userText
   	    userText = raw_input("Enter text ("" to quit): ")

if __name__ == "__main__":
    main()
    
