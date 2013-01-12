#!/usr/bin/env python
"""CURSES EXAMPLE, by Richard White, 2012-01-03
"""

import curses

def main(stdscr):
    stdscr.addstr(0,2,"Curses example: h)left, l)right, q)uit")
    # Set play area to 80 characters wide
    horzPosition = 19
    while True:
        stdscr.addch(3, horzPosition,'@')
        stdscr.refresh()
        a_char_code = stdscr.getch()
        if chr(a_char_code) == "q":
            break
        elif chr(a_char_code) == "h":
            stdscr.addch(3, horzPosition,' ')
            horzPosition -= 1
        elif chr(a_char_code) == "l":
            stdscr.addch(3, horzPosition,' ')
            horzPosition += 1
        if horzPosition < 0:
            horzPosition = 0
        elif horzPosition > 39:
            horzPosition = 39


if __name__ == "__main__":
    curses.wrapper(main)

