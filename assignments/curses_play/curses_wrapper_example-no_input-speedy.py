#!usr/bin/env python

import curses

def main(stdscr):
    screenWidth = 80
    horzPosition = 39
    delta = +1
    while True:
        stdscr.addch(0, horzPosition,'@')
        stdscr.refresh()
        stdscr.addch(0, horzPosition,' ')
        horzPosition += delta
        if horzPosition > 78:
            delta = -1
        elif horzPosition < 1:
            delta = +1

if __name__ == "__main__":
    curses.wrapper(main)
