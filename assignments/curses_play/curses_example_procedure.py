#!/usr/bin/python

# Information on using "curses" to control display is available online at
# http://docs.python.org/howto/curses.html#curses-howto
# and at
# http://heather.cs.ucdavis.edu/~matloff/Python/PyCurses.pdf

import curses, traceback

def initscreen():
    stdscr = curses.initscr()   # returns a window object representing the screen
    curses.noecho()             # turns off auto echo of key input
    curses.cbreak()             # allows computer to process key without [Enter]
    stdscr.keypad(1)            # enables keypad mode
    curses.start_color()        
    return stdscr

def restorescreen(stdcr):
    curses.nocbreak();
    curses.echo()               # reverses terminal settings
    curses.endwin()             # restores terminal
    stdscr.keypad(0)

def main(stdscr):
    stdscr.clear()              # clear the screen
    stdscr.addch(0,0,'0')       # place a character at height,width
    stdscr.refresh()            # update the whole screen
    while True:
        a_char_code = stdscr.getch()    # get input from user (no echo)
        a_char = chr(a_char_code)       # convert to a character
        if a_char == 'q': break
        stdscr.addch(0,0,a_char)   # place that character at location 

if __name__ == '__main__':
    try:
        stdscr = initscreen()
        main(stdscr)
        restorescreen(stdscr)
    except:
        restorescreen(stdscr)
        traceback.print_exc()
        
