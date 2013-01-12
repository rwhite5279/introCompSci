#!/usr/bin/env python
"""
rogue3.py, by Richard White, 2012-05-04
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
    for y in range(height):
        screen[0][y] = "|"
        screen[width-1][y] = "|"
    return screen

# -----------------------------------------------------------------------------
            
def initRooms(screen, stdscr):
    """This function creates four semi-random rectangular rooms on the screen by defining 2 points per room: upperLeft and lowerRight grid points."""
    import time

    def putRoomInScreen(screen,upperLeftX,upperLeftY,lowerRightX,lowerRightY):
        for x in range(upperLeftX,lowerRightX+1):
            screen[x][upperLeftY] = '-'
            screen[x][lowerRightY] = '-'
        for y in range(upperLeftY+1, lowerRightY):
            screen[upperLeftX][y] = '|'
            screen[lowerRightX][y] = '|'
     
    def createRoom(screen):
        rooms = []
        xLimit = 2   # These are the jumping off points for the upperLeft coords
        yLimit = 2   # of the first room.
        for room in range(3):
            upperLeftX = random.randrange(xLimit,xLimit + 6 + int(len(screen)/6.0))
            upperLeftY = random.randrange(yLimit,yLimit + 4 + int(len(screen[0])/6.0))
            xLimit = upperLeftX + 3
            yLimit = upperLeftY + 3
            lowerRightX = random.randrange(xLimit,xLimit + 6 + int(len(screen)/6.0)) 
            lowerRightY = random.randrange(yLimit,yLimit + 4 + int(len(screen[0])/6.0))
            lowerRightX = min(lowerRightX,len(screen)-2)
            # if random.randrange(0,2) == 0:
            #     walkerCurrent = [random.randrange(upperLeftX,lowerRightX),random.randrange(upperLeftY,lowerRightY)]
            #     screen[walkerCurrent[0]][walkerCurrent[1]] = "@"
            putRoomInScreen(screen,upperLeftX,upperLeftY,lowerRightX,lowerRightY)
            stdscr.addstr(0,0,str(upperLeftX)+','+str(upperLeftY)+'//'+str(lowerRightX)+','+str(lowerRightY))
            xLimit = lowerRightX + 3
            yLimit = 2
            walkerCurrent = 0 
        return walkerCurrent    

    walkerCurrent = createRoom(screen)           
    return walkerCurrent
       
def corral(screen,walkerCurrent,walkerNext):
    """
    walkerCurrent is a x-y tuple, as is walkerNext
    screen is a 2-d list of lists, with '-' representing horizontal
    boundaries and '|' representing vertical boundaries. '+' represents
    a navigable doorway, and '.' represents a legal move. All other
    position/monster codes are not traversable.
    len(screen) is the width, and len(screen[0]) is the height of the grid
    """
    # Check to see if walker is in screen boundaries (including wall)
    if walkerCurrent[0] == 0 \
        or walkerCurrent[0] == len(screen) \
        or walkerCurrent[1] == 0 \
        or walkerCurrent[1] == len(screen[0]):
        return -1
    elif screen[walkerNext[0]] in ['+','.'] \
        and screen[walkerNext[1]] in ['+','.']:
        return walkerNext   # as new location
    else:
        return walkerCurrent # walker was unable to be moved
        

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
    walkerCurrent = initRooms(theScreen,stdscr)
    printScreen(theScreen,stdscr)
    while True:
        ch = stdscr.getch()         # Checks to see if a key has been pressed
        if chr(ch) == "q": break    # If the character of that key code is the
                                    # letter q, end program
        elif chr(ch) == "a":
            pass    
        elif chr(ch) == "w":
            pass
        elif chr(ch) == "d":
            pass    
        elif chr(ch) == "s":
            pass


# -----------------------------------------------------------------------------  

if __name__ == "__main__":
    curses.wrapper(main)   
    
