#!/usr/bin/env python
"""
rogue5.py, by Richard White, 2012-05-04

This version is going to attempt to implement a Model-View-Controller approach.

Here, although I've got routines set up to create the curses-based graphics, I'm not actually using those routines yet. Here, I'm more interested in the Model aspect of the data: what does the data representation of the items in the game look like?

"initItems" and "displayItems" is set to try out this idea.

The next step is to write a routine that goes through the items list and displays those items on the screen, if appropriate.

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
    # height,width = stdscr.getmaxyx()  # Get height & width of current screen
    # height = height - 1     # Adjust height so we never print at bottom
                            # (It freaks out the display on last character)
    height = 20
    width = 80
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
            
def initItems():
    """
    This function establish the walker, some rooms, and some items for initial testing.
    """
    items=[]
    """Fields: 
        item#,
        'name',
        'class (of object),
        'display character',
        level,
        [locationX,locationY],
        displayBit (0 or 1)"""
    adventurer = [0,'Adam','adventurer','@',1,[20,10],1]
    items.append(adventurer)
    """Fields: 
        item#,
        'name',
        'class (of object)',
        'display character',
        level,
        [upperLeft[X,Y],lowerRight[X,Y], door1,door2,door3,door4],
        displayBit (0 or 1)"""
    room = [1,'Room 1','room','',1,[[18,8],[23,12],[[20,8],[23,10],[],[18,10]]],1]
    items.append(room)
    return items

# -----------------------------------------------------------------------------

def displayItems(items):        # Diagnostic routine for debugging
    for item in items:
        print item

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
    printScreen(theScreen,stdscr)
    while True:
        ch = stdscr.getch()         # Checks to see if a key has been pressed
        if chr(ch) == "q": break    # If the character of that key code is the
                                    # letter q, end program
        elif chr(ch) in ('a','s','w','d'):
            pass 
            
# -----------------------------------------------------------------------------  

if __name__ == "__main__":
    # curses.wrapper(main)   
    items = initItems() 
    displayItems(items)




