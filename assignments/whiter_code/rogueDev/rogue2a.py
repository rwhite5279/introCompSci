#!/usr/bin/env python
"""
rogue2.py, by Richard White, 2012-05-04
This program is the second step in writing a Rogue-style game. The series of programs details--step-by-step, feature-by-feature--how to go about implementing a text-based game.
This second version of the program, rogue2, creates a series of 4 semi-random "rooms" on the screen that will be traveled through by the user and monsters.
Note that the screen locations are listed as y,x, where y is how many lines down from top (0 to whatever), and x is how many columns over from left (0 to whatever).
Information on using "curses" to control display is available online at
http://docs.python.org/howto/curses.html#curses-howto
and at
http://heather.cs.ucdavis.edu/~matloff/Python/PyCurses.pdf
"""

import curses
import random

# -----------------------------------------------------------------------------

def initScreen(stdscr):
    screen=[]
    height,width = stdscr.getmaxyx()  # Get height & width of current screen
    height = height - 1     # Adjust height so we never print at bottom
                            # (It freaks out the display on last character)
    for x in range(width):
        screen.append(['.']*(height))   # initalize list for room column y
    # Set up horizontal walls at row 0 and row 'height-1'
    for x in range(width):
        screen[x][0] = '-'
        screen[x][height-1] = '-'
    # Set up vertical walls at column 0 and column 'width-1'
    for y in range(1,height-1):
        screen[0][y] = "|"
        screen[width-1][y] = "|"
    return screen

# -----------------------------------------------------------------------------
            
def createRoom(screen, doorLocation, roomOrientation, stdscr, placeWalker=False):
    """This function creates a room beginning at a location on the screen, which is where a door is defined for the room. The function also places 4 doors in the walls, a monster or 2, money, potion, scroll, based on randomness, and puts the character in there if the optional parameter placeWalker is True."""
    if roomOrientation == 'down':    # We've created a door, and need to create a room below it
        upperLeftY = doorLocation[1]
        lowerRightY = upperLeftY + random.randrange(5,7)
        upperLeftX = doorLocation[0] - random.randrange(2,6)
        lowerRightX = doorLocation[0] + random.randrange(2,6)
    if roomOrientation == 'up':      # Create room above door
        lowerRightY = doorLocation[1]
        upperLeftY = lowerRightY - random.randrange(5,7)
        upperLeftX = doorLocation[0] - random.randrange(2,6)
        lowerRightX = doorLocation[0] + random.randrange(2,6)
    if roomOrientation == 'left':    # Create room to left of door
        lowerRightX = doorLocation[0]
        upperLeftX = lowerRightX - random.randrange(5,7)
        upperLeftY = doorLocation[1] - random.randrange(2,4)
        lowerRightY = doorLocation[1] + random.randrange(2,4)   
    if roomOrientation == 'right':   # Create room to right of door
        upperLeftX = doorLocation[0]
        lowerRightX = upperLeftX + random.randrange(5,7)
        upperLeftY = doorLocation[1] - random.randrange(2,4)
        lowerRightY = doorLocation[1] + random.randrange(2,4)
    
    # Put the room into the screen
    for x in range(upperLeftX,lowerRightX+1):
        screen[x][upperLeftY] = '-'
        screen[x][lowerRightY] = '-'
    for y in range(upperLeftY+1, lowerRightY):
        screen[upperLeftX][y] = '|'
        screen[lowerRightX][y] = '|'
    
    # Place additional doors as necessary                           
    if roomOrientation in ('down','left','up'):   
        if upperLeftX > 15:             # if there's space for a room to the left
            screen[upperLeftX][random.randrange(upperLeftY+1, lowerRightY)] = '<'
    if roomOrientation in ('down','right','up'):
        if len(screen) - lowerRightX > 15:  # if there's space to the right
            screen[lowerRightX][random.randrange(upperLeftY+1, lowerRightY)] = '>'
    if roomOrientation in ('left','right','up'):
        if upperLeftY > 10:              # if there's space at the top
            screen[random.randrange(upperLeftX+1, lowerRightX)][upperLeftY] = '^'  
    if roomOrientation in ('left','right','down'):   
        if len(screen[0]) - lowerRightY > 10:    # if there's space at the bottom
            screen[random.randrange(upperLeftX+1, lowerRightX)][lowerRightY] = 'V'

    # Place Walker
    if placeWalker:
        walker = [random.randrange(upperLeftX+1,lowerRightX), \
            random.randrange(upperLeftY+1,lowerRightY)]
        screen[walker[0]][walker[1]] = '@'
        screen[doorLocation[0]][doorLocation[1]] = "+"

# -----------------------------------------------------------------------------
            
def printScreen(screen, stdscr):
    for y in range(len(screen[0])):
        for x in range(len(screen)):
            stdscr.addch(y,x,screen[x][y])
    stdscr.addstr(0,len(screen)/2-5,'R O G U E')
    stdscr.refresh()    # Draw screen
        
# -----------------------------------------------------------------------------  

def main(stdscr):
    theScreen = initScreen(stdscr)
    createRoom(theScreen,(15,15),'right',stdscr, True)
    printScreen(theScreen,stdscr)
    while True:
        ch = stdscr.getch()         # Checks to see if a key has been pressed
        if chr(ch) == "q": break    # If the character of that key code is the
                                    # letter q, end program

# -----------------------------------------------------------------------------  

if __name__ == "__main__":
    curses.wrapper(main)   
    
