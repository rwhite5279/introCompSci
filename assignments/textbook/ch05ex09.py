#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 5, Programming Exercise #9
# Write a program that counts the number of words in a sentance entered by the user.



































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the input from the user, a sentence
#    Split the sentence up into words (how?!
#         There are lots of different strategies)
#    Tell how many words there were

# Call the main function
































# -------------- PROGRAM -----------------------

# ch05ex05.py, Chapter 5, Exercise 9
# From Zelle's Python Programming, Chapter 5
# By Richard White
# 2011-02-11

# This program find out how many words there are in a sentence, in a few different ways.

def main():
    
    sentence = raw_input("Please enter a sentence, and I'll tell you how many words there are in it: ")
    print "First, I'll count the words by counting the spaces in between them:"
    num_of_words1 = sentence.count(" ") + 1  # Why did we have to add 1?!
    print num_of_words1
    print "Now, I'll count the words by separating the sentence into individual words."
    # This next line uses the split function to split the sentence into a list of words, then
    # counts the words in that list.
    num_of_words2 = len(sentence.split())
    print num_of_words2
    print "Now, I'll count the words the hard way by going through the characters, and keeping track"
    print "of how many spaces I find."
    num_of_spaces = 0
    for char in sentence:
        if char == " ":
            num_of_spaces = num_of_spaces + 1
    num_of_words3 = num_of_spaces + 1
    print num_of_words3

main ()










