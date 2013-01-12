#!/usr/bin/env python
"""
rogue1.py, by Richard White, 2012-05-04

This program is the first step in writing a Rogue-style game. The series of programs details--step-by-step, feature-by-feature--how to go about implementing a text-based game.

This first version of the program, rogue1, simply demonstrates how to use curses to initiate a character-based interface.

Note that the screen locations are listed as y,x, where y is how many lines down from top (0 to whatever), and x is how many columns over from left (0 to whatever).

Information on using "curses" to control display is available online at
http://docs.python.org/howto/curses.html#curses-howto
and at
http://heather.cs.ucdavis.edu/~matloff/Python/PyCurses.pdf
"""

import curses

# -----------------------------------------------------------------------------

def initScreen(stdscr):
    """
    This uses the 'stdscr' attribute from curses, and pulls in screen dimension height and width so that we can initialize a screen area that matches the dimensions of the terminal window. 
    """
    screen=[]
    height,width = stdscr.getmaxyx()  # Get height & width of current screen
    height = height - 1     # Adjust height so we never print at bottom
                            # (It freaks out the display on last character)
    """
    We'll set up a screen[x][y] "list of lists" to refer to each location in the screen, where x runs along the horizontal axis and y runs from 0 to height DOWN the vertical.

    0,0 ---------------------------------------------------25,0
    0,1 ---------------------------------------------------25,1
    0,2 ---------------------------------------------------25,2
    .
    .
    .
    0,15 --------------------------------------------------25,15
    """
   
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
            
def printScreen(screen, stdscr):
    """
    The tricky thing about printing the screen is that the the addch and addstr methods, used to add a character or a string at a specified location, specify based on a y,x coordinate, BACKWARDS from the [x],[y] that is standard for this kind of thing. So the lower right corner of our screen, which we consider 25,15 in data form, would be addressed as addch(15,25,'x') if we wanted to place the character x there. Weird, huh?
    """
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
        pass

# -----------------------------------------------------------------------------  

if __name__ == "__main__":
    curses.wrapper(main)   
    """ curses.wrapper allows us to call the main function and pass it the paramater stdscr, which may then be used to refer to the curses screen. The wrapper automatically turns on and off various modes that allow for curses to opereate as it should, and (most importantly) autorestores those modes to their original state in the terminal window if there's an error."""
    
