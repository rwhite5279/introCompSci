#!/usr/bin/env python
"""
rogue8.py, by Richard White, 2012-05-11
A Model-View-Controller approach

The next step is to only allow the Adventurer to make legal moves, according to room boundaries that have been set up in the items list. A move is allowed if it's within the boundaries of the room. (We'll deal with monsters and picking up items later on.) 

Information on using "curses" to control display is available online at
http://docs.python.org/howto/curses.html#curses-howto
and at
http://heather.cs.ucdavis.edu/~matloff/Python/PyCurses.pdf
"""
import curses
import random
# -------------------------------------------------------------------------
def initScreen(stdscr):     # View function
    """ Creates a new screen everytime."""
    screen=[]
    height = 20
    width = 80
    for x in range(width):
        screen.append([' ']*(height))   # initalize list for room column y
    # Set up horizontal walls at row 0 and row 'height-1'
    for x in range(width):
        screen[x][0] = '-'
        screen[x][height-1] = '-'
    # Set up vertical walls at column 0 and column 'width-1'
    for y in range(1,height-1):
        screen[0][y] = "|"
        screen[width-1][y] = "|"
    return screen
# -------------------------------------------------------------------------
def initItems():            # Model function
    """Runs only once at beginning of program. This is currenlty happening
    manually, although it can by dynamically generated at some point too."""
    items=[]
    """Fields:item#,'name','class (of object),'display character',level,roomID,[locationX,locationY],displayBit (0 or 1)"""
    adventurer = [0,'Adam','adventurer','@',1,1,[20,10],1]
    items.append(adventurer)
    """Fields: item#,'name','class (of object)','display character',level,roomID(unused),[upperLeft[X,Y],lowerRight[X,Y],door1,door2,door3,door4],displayBit(0 or 1)"""
    room = [1,'Room 1','room','',1,-1,[[18,8],[23,12],[[20,8],[23,10],[],[18,10]]],1]
    items.append(room)
    room = [2,'Room 2','room','',1,-1,[[26,6],[31,11],[[28,6],[30,11],[26,8],[31,9]]],1]
    items.append(room)
    scroll = [3,'Invisibility Scroll','object','!',1,1,[19,9],1]
    items.append(scroll)
    monster = [4,'Troll','monster','T',1,2,[28,8],1]
    items.append(monster)
    return items
# -------------------------------------------------------------------------
def addItemsToScreen(items,screen,stdscr):     # View function
    def displayRoom(room,screen):   # displaying a room and doors
                                    # list of upperLeft, lowerRight coords,
                                    # and locations of doors
        for j in range(room[0][1],room[1][1]+1): # Y coordinate down 
            screen[room[0][0]][j] = '|'
            screen[room[1][0]][j] = '|'
        for i in range(room[0][0],room[1][0]+1): # X coordinate across
            screen[i][room[0][1]] = '-'
            screen[i][room[1][1]] = '-'
        # display doors now
        for door in room[2]:
            if len(door) > 0: screen[door[0]][door[1]] = '+'
    # Find out what level adventurer is on
    level = items[0][4]
    location = items[0][6]
    # Install rooms for that level
    for item in items:
        if item[2] == 'room' and item[4] == level and item[7] == 1:
            displayRoom(item[6],screen)        
    # Place objects in rooms
    for item in items:
        if item[2] == 'object' and item[4] == level and item[7] == 1:
            screen[item[6][0]][item[6][1]] = item[3]
    # Place monsters in rooms
    for item in items:
        if item[2] == 'monster' and item[4] == level and item[7] == 1:
            screen[item[6][0]][item[6][1]] = item[3]
    # Place adventurer last!
    screen[location[0]][location[1]] = '@'
# -------------------------------------------------------------------------
def interact(move,items):        # Model function
    """Check to see if there's anything on this level at that location.
        If it's a wall, stay where you are.
        If it's a door, move onto it.
        If it's an object, move onto it and get it.
        If it's a monster, fight it.
        """
    currentLevel = items[0][4]      # Gets adventurer's current level
    currentRoom = items[0][5]       # Gets adventurer's current room
    currentLoc = items[0][6]        # GEts adventurer's current location
    # Identify desired new location
    if move == 'a': newLoc = currentLoc[0] - 1,currentLoc[1]
    elif move == 's': newLoc = currentLoc[0],currentLoc[1] + 1
    elif move == 'd': newLoc = currentLoc[0] + 1,currentLoc[1]
    elif move == 'w': newLoc = currentLoc[0],currentLoc[1] - 1
    # test for a wall 
    for item in items:
        if item[0] == currentRoom:   # Adventurer is in Room item[0]!
            if newLoc[0] > item[6][0][0] and \
               newLoc[0] < item[6][1][0] and \
               newLoc[1] > item[6][0][1] and \
               newLoc[1] < item[6][1][1]:
                items[0][6] = newLoc    # Reset's adventurer's location
            # test for a door
            else:
                door = False
                for i in range(4):
                    if len(item[6][2][i]) > 0:
                        if item[6][2][i][0] == newLoc[0] and \
                           item[6][2][i][1] == newLoc[1]:
                            door = True
                if door: 
                    items[0][6] = [newLoc[0],newLoc[1]]
    # test for an object(scroll, potion, weapon, etc.)
    # test for a monster
# -------------------------------------------------------------------------
def printScreen(stdscr, items):     # View function
    screen = initScreen(stdscr)     # Initialize screen every time to clear
    addItemsToScreen(items,screen,stdscr)
    for y in range(len(screen[0])):
        for x in range(len(screen)):
            stdscr.addch(y,x,screen[x][y])  # Place on actual screen what at screen[x][y]
    stdscr.addstr(0,len(screen)/2-5,'R O G U E')    # Title bar
    stdscr.addstr(0,3,str(items[0][6][0])+','+str(items[0][6][1])) # Walker loc
    stdscr.refresh()    # Draw screen
# -------------------------------------------------------------------------  
def main(stdscr):
    items = initItems()
    printScreen(stdscr,items)
    while True:
        ch = stdscr.getch()         # Checks to see if a key has been pressed
        if chr(ch) == "q": break    # If the character of that key code is the
                                    # letter q, end program
        elif chr(ch) in ('a','s','w','d'):
            interact(chr(ch),items) 
        printScreen(stdscr,items)
# -------------------------------------------------------------------------  
if __name__ == "__main__":
    curses.wrapper(main)   

