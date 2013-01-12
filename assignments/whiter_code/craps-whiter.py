#!/usr/bin/env/ python
"""
PROGRAMMING ASSIGNMENT for 2012-02
CRAPS-PLAYING PROGRAM

The basic rules for playing craps are relatively simple:
1. A player rolls two six-sided dice and adds the numbers rolled together.
2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12
   automatically loses, and play is over. If a 4, 5, 6, 8, 9, or 10 are
   rolled on this first roll, that number becomes the "point."
3. The player continues to roll the two dice again until one of two things
   happens: either they roll the "point" again, in which case they win; or
   they roll a 7, in which case they lose.

Write a program that allows a user to play the game of craps on the
computer.
"""


































































# PSEUDOCODE FOR CRAPS-PLAYING PROGRAM

# Roll two dice for the user and add their faces together
# If they got a 7 or 11:
#     they win!
# If they got a 2, 3, or 12:
#     they lose!
# If they got anything else:
#     Remember the point value
#     Have them keep rolling until:
#         They roll the point again, and win!
#     or
#         They roll a 7, and lose!






































































#!/bin/usr/python
# CRAPS-PLAYING PROGRAM
# Richard White, 2012-02-18

# ------------------------DICE ROLLING FUNCTION---------------------------

def roll_two_dice():
    import random    
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1 + die2

# ------------------------MAIN FUNCTION---------------------------

def main():
    play_game = raw_input("Would you like to play the game of Craps? (Y/n)")
    if play_game == "": play_game = "y"
    if play_game[0].lower() != "n":
        instructions = raw_input("Do you need instructions? (y/N)")
        if instructions == "": instructions = "n"
        if (instructions[0].lower() != "n"):
            print "1. A player rolls two six-sided dice and adds the numbers rolled together."
            print "2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12"
            print "   automatically loses, and play is over. If a 4, 5, 6, 8, 9, or 10 are "
            print "   rolled on this first roll, that number becomes the 'point.'"
            print "3. The player continues to roll the two dice again until one of two things"
            print "   happens: either they roll the 'point' again, in which case they win; or"
            print "   they roll a 7, in which case they lose."
    while (play_game[0].lower() != "n"):
        pause = raw_input("Press <Enter> to roll the dice!"),
        first_roll = roll_two_dice()
        print "You rolled a",first_roll,"on your first roll..."
        # Check to see if they won or lost
        if first_roll == 7 or first_roll == 11:
            print "You WON!!!"
        elif first_roll == 2 or first_roll == 3 or first_roll == 12:
            print "You lost... :("
        else:     # They didn't win on first roll--try to make the point
            print "That's your point. Try to roll it again before you roll 7 and lose!"
            done = False
            while (not done):
                pause = raw_input("Press <Enter> to roll the dice!"),
                point_roll = roll_two_dice()
                print "You rolled a",point_roll
                if first_roll == point_roll:
                    print "You rolled your point and WON!"
                    done = True
                elif point_roll == 7:
                    print "You rolled a 7 and lost!!!"
                    done = True
                else:
                    print "Keep on rolling..."
        play_game = raw_input("Wanna play again? (Y/n)")
        if play_game == "": play_game = "y"
    print "Thanks for visiting! See you next time!"
    
# ------------------------START THE PROGRAM---------------------------

if __name__ == "__main__":
    main()


