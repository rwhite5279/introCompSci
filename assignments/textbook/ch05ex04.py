#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 5, Programming Exercise #4
# An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For example, RAM is an acronym for "random access memory." Write a program that allows the user to type ina phrase and then outputs the acronym for that phrase. Note: the acronym should be all uppercase, even if the words in the phrase are not capitalized.


























# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get the input from the user, a string
#    Split the string up into individual words
#    Get the first letter of each word, and then print it out, capitalized

# Call the main function






















# -------------- PROGRAM -----------------------

# ch05ex04.py, Chapter 5, Exercise 4
# From Zelle's Python Programming, Chapter 5
# By Richard White
# 2009-07-02

# This program prints out capitalized acronyms for a string entered

def main():

    import string   # needs this for split and capitalize functions
    
    user_string = raw_input("Please enter a multi-word string: ")
    word_list = string.split(user_string," ")
    acronym = ""
    for word in word_list:
        acronym = acronym + string.capitalize(word[0])
    print "Your acronym is",acronym     

main ()
