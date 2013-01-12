#!/usr/bin/python
"""mugwump.py, by Richard White
This program allows the user to play the game of Mugwump.

Problem (available online at http://www.atariarchives.org/basicgames/showpage.php?page=114)
Your objective in this game is to find the four Mugwumps hiding on various squares of a 10-by-10
grid. Homebase (lower left) is position (0,0) and a guess is a pair of whole numbers (0 to 9),
separated by commas. The first number is the number of units to the right of homebase and the
second number is the distance above homebase.
You get ten guesses to locate the four Mugwumps; after each guess, the computer tells you how
close you are to each Mugwump. Playing the game with the aid of graph paper and a compass should
allow you to find all the Mugwumps in six or seven moves using triangulation.
If you want to make the game somewhat more difficult, you can print the distance to each Mugwump
either rounded or truncated to the nearest integer.
This program was modified slightly by Bob Albrecht of People's Computer Company. It was originally
written by students of Bud Valeni of Project SOLO in Pittsburgh, Pennsylania.

Sample Input/Output:
TURN NO. 5. What is your guess? 8,8
You are 3.1 units from Mugwump 1
You are 4 units from Mugwump 2
You have found Mugwump 3
You are 8.5 units from Mugwump 4
"""













































# INTRO PSEUDOCODE

# Initialize the board as a 10-by-10 "list of lists"
# Place 4 mugwumps randomly on the board
# Ask user to enter their guess
# Calculate the distance to each Mugwump and report
# If distance is 0 for any Mugwumps, indicate that they've been found
# Keep going until a) all Mugwumps have been found, or b) 10 tries have elapsed.






















































# ADVANCED PSEUDOCODE

#import random

#def give_instructions():

#def initialize_game(board,mugwump):
#    """Board is 10x10, and needs to have 4 random locations for Mugwumps. Although it's not strictly necessary to play the game, we'll create a 2-dimensional array (a list of lists, actually), with characters stored at each point on the grid to assist the user visually."""
    # Initialize board
    # for j in range(0,10):
        # Adds an empty list item to b
        #for i in range(0,10):
            # Adds to the list another item, all of which are zeroes to begin with
    # Initialize Mugwump locations
    #for k in range (0,4):  # Go through each mugwump and initialize him to a random location.
        # Create 4 empty lists, one for each mugwump
        # Store location of mugwump as a list
        # Mugwump look like this now: [[3, 1], [5, 4], [2, 4], [2, 8]]
        # Indicate locations of Mugwumps on the board with a 1, 2, 3, 4
        

#def print_board(board):


# def play_game(board,mugwump):
    # for turn in range(1,11):
        # Get coordinates for user's guess
        # for k in range(0,4):       # Check and report distance to each mugwump
            # If we haven't found this mugwump
                # distance = ((x_guess - mugwump[k][0])**2 + (y_guess - mugwump[k][1])**2)**0.5
                # if distance to this mugwump is 0
                    #print "You found Mugwump #",k+1,"!!!!"
                    #mugwump[k][0] = -1    # This indicates that he's been found
                    #num_found += 1
                # else:
                    # print "Distance to Mugwump #",k+1,"is",distance
        #if (num_found >= 4):
            #finished = True
            #break
        


# def main():
    # board=[]
    #mugwump=[]
    #give_instructions()
    #initialize_game(board,mugwump)
    #print_board(board)         # You can choose to print the board for debugging/cheating purposes
    #play_game(board,mugwump)


# if __name__ == "__main__":
#     main()













































# Mugwumps Program
# by Richard White
# 2010-01-18

import random

def give_instructions():
    print "Let's play Mugwump!"
    want_instructions = raw_input("Do you want instructions (y/N)?")
    if want_instructions == '':   # See if you can figure out why we put this in here!
        return
    elif (want_instructions.lower()[0] == 'y'):
        print "Here's how you play:"
        print "Four Mugwumps are hiding underground in a 10 x 10 area."
        print "I'll ask you to enter a location that you want to look for them,"
        print "and you can enter a 2 digit code, like this: 0,9. I'll then tell"
        print "you how far away each of the Mugwumps is from you. You only have"
        print "ten guesses to find them all!"
        print 
        print "Good luck!"
        print
        

def initialize_game(board,mugwump):
    """Board is 10x10, and needs to have 4 random locations for Mugwumps. Although it's not strictly necessary to play the game, we'll create a 2-dimensional array (a list of lists, actually), with characters stored at each point on the grid to assist the user visually."""
    # Initialize board
    for j in range(0,10):
        board.append([]) # Adds an empty list item to b
        for i in range(0,10):
            board[j].append(0)  # Adds to the list another item, all of which are zeroes to begin with
    # Initialize Mugwump locations
    for k in range (0,4):  # Go through each mugwump and initialize him to a random location.
        mugwump.append([]) # Create 4 empty lists, one for each mugwump
        randx=random.randrange(0,10)
        randy=random.randrange(0,10)
        mugwump[k] = [randx,randy]  # Store location of mugwump as a list
                                    # Mugwump look like this now: [[3, 1], [5, 4], [2, 4], [2, 8]]
        board[randx][randy] = k+1   # Indicate locations of Mugwumps on the board with a 1, 2, 3, 4
        

def print_board(board):
    for j in range(9,-1,-1):
        print j ,"|",
        for i in range (0,10):
            print board[i][j],
        print
    print "  +---------------------"
    print "   ", 
    for i in range(0,10):
        print i,
    print


def play_game(board,mugwump):
    finished = False
    num_found = 0
    print "Here we go!"
    for turn in range(1,11):
        print "It's turn #",turn
        coords = raw_input("Where do you want to check for a Mugwump (x,y)?")
        x_guess = eval(coords)[0]    # Converts string coordinates into a tuple
        y_guess = eval(coords)[1]
        for k in range(0,4):       # Check and report distance to each mugwump
            if (mugwump[k][0] != -1):    # We'll use the x-component = -1 to indicate if it's been found
                distance = ((x_guess - mugwump[k][0])**2 + (y_guess - mugwump[k][1])**2)**0.5
                if (distance == 0):
                    print "You found Mugwump #",k+1,"!!!!"
                    mugwump[k][0] = -1    # This indicates that he's been found
                    num_found += 1
                else:
                    print "Distance to Mugwump #",k+1,"is",distance
        if (num_found >= 4):
            finished = True
            break
    if (finished == True):
        print "Congratulations! You found all the Mugwumps!"
    else:
        print "I'm sorry! You didn't find all the Mugwumps!"
        print "Here's where they were hiding..."
        print_board(board)
        


def main():
    board=[]
    mugwump=[]
    give_instructions()
    initialize_game(board,mugwump)
    print_board(board)         # You can choose to print the board for debugging/cheating purposes
    play_game(board,mugwump)


if __name__ == "__main__":
    main()
