#!/usr/bin/env python
"""
rogue6.py, by Richard White, 2012-05-04

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
    Ultimately, once this is all set up, this initItems will simply fill the items list with a list of pre-approved items. Additional items (rooms, monsters, objects) can be added to the list dynamically as necessary.
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
    scroll = [2,'Invisibility Scroll','object','!',1,[19,9],1]
    items.append(scroll)
    return items

# -----------------------------------------------------------------------------

def displayItems(items):        # Diagnostic routine for debugging
    for item in items:
        print item

# -----------------------------------------------------------------------------

def addItemsToScreen(items,screen):

    def displayRoom(room,screen):  # takes care of displaying a room and doors
                            # input is list of upperLeft and lowerRight coords,
                            # and locations of doors
        for j in range(room[0][1],room[1][1]+1): # Y coordinate down screen
            screen[room[0][0]][j] = '|'
            screen[room[1][0]][j] = '|'
        for i in range(room[0][0],room[1][0]+1): # X coordinate across screen
            screen[i][room[0][1]] = '-'
            screen[i][room[1][1]] = '-'
        # display doors now
        for door in room[2]:
            if len(door) > 0: screen[door[0]][door[1]] = '+'

    # Find out what level adventurer is on
    for item in items:
        if item[0] == 0: 
            level = item[4]
            screen[item[5][0]][item[5][1]] = '@'

    # Install rooms for that level
    for item in items:
        if item[2] == 'room' and item[4] == level: 
            displayRoom(item[5],screen)        

    # Place objects in rooms
    for item in items:
        if item[2] == 'object' and item[4] == level:
            screen[item[5][0]][item[5][1]] = item[3]


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
    items = initItems()
    addItemsToScreen(items,theScreen)
    printScreen(theScreen,stdscr)
    while True:
        ch = stdscr.getch()         # Checks to see if a key has been pressed
        if chr(ch) == "q": break    # If the character of that key code is the
                                    # letter q, end program
        elif chr(ch) in ('a','s','w','d'):
            pass 
            
# -----------------------------------------------------------------------------  

if __name__ == "__main__":
    curses.wrapper(main)   
