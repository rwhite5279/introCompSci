#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 11, Programming Exercise #6
# Write and test a function shuffle(myList) that scrambles a list into a random order, like shuffling a deck of cards.














































# -------------- PSEUDO CODE -------------------

# Define the function shuffle()

#    Get a list (maybe fill the list up with letters or numbers, in order?)
#    For entire list:
#        Get a random item from the list, remove it, and append it to a second list
#    Replace the first list with the one we just created

# Call the function shuffle()
















































# -------------- PROGRAM -----------------------

# ch11ex06.py, Chapter 11, Exercise 6
# From Zelle's Python Programming, Chapter 11
# By Richard White
# 2011-02-14

# This program takes a list of items and shuffles them.

import random

def shuffle():
    # We don't quite know how to pass in lists as parameters to a function just yet, so this will just work internally.
    # Create an ordered list of items. Say, the integers from 1 to 52?
    myList = []   # creates an empty list
    for i in range(52):
        myList.append(i)    # puts 0 in myList[0], 1 in myList[1], 2 in myList[2], etc.
    print "The original list looks like this:"
    print myList
    print "Now let's shuffle it."
    # Use random function to get a random "card" from the list, and append it to the new list. We also
    # have to make sure to remove it from the old one. The pop() method is perfect for this.
    
    # There are lots of different ways to go through the list of current cards. Watch how this "while" loop does it.
    newList = []   # initializes the new list
    while len(myList) > 0:
        whichCard = random.randrange(len(myList))   # Gets a randomly numbered card from the current myList
        newList.append(myList.pop(whichCard))       # Wow! Take a moment to figure out what that statement did.
                                                    # Take the random # of our chosen card, pop that card from
                                                    # myList, and append it to the newList. Cool.
    print "The new list looks like this:"
    print newList
    
	
	
shuffle()
