#!/usr/bin/env python
"""CURSES EXAMPLE, by Richard White, 2012-01-03
"""

import curses
import time

def main(stdscr):
    stdscr.addstr(0,2,"Curses example: h)left, l)right, q)uit")
    horzPosition = 19
    delta = 0
    while True:
		stdscr.refresh()
		stdscr.nodelay(1)
		while True:
			a_char_code = stdscr.getch()
			if a_char_code != -1:
				break
			stdscr.addstr(3,horzPosition," ")
			horzPosition += delta
			if horzPosition < 0:
				horzPosition = 0
			elif horzPosition > 39:
				horzPosition = 39
			stdscr.addstr(3,horzPosition,'@')
			stdscr.refresh()
			time.sleep(0.02)
		stdscr.nodelay(0)
		if chr(a_char_code) == "q":
			break
		elif chr(a_char_code) == "h":
			delta = -1
		elif chr(a_char_code) == "l":
			delta = +1

if __name__ == "__main__":
    curses.wrapper(main)

