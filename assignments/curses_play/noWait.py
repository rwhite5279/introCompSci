#!/usr/bin/env python
"""Get nodelay working?"""
import curses

def main(stdscr):
    while True:
        aChar = chr(stdscr.getch())
        stdscr.addstr(0,0,"You've begun the program...")
        stdscr.refresh()
        stdscr.nodelay(1)
        while True:
            aCode = stdscr.getch()
            if aCode != -1:
                break    # If we haven't gotten legit input...
            stdscr.addstr(0,0,'|')
            stdscr.refresh()
            stdscr.addstr(0,0,'-')
            stdscr.refresh()
        # Once we break out of loop (having gotten a key input)
        stdscr.nodelay(0)
        aChar = stdscr.getch()
        
if __name__ == "__main__":
    curses.wrapper(main)
